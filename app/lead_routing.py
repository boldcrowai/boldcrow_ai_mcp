import json
import logging
import smtplib
import ssl
from email.mime.text import MIMEText
from typing import Any, Dict, List, Optional, Tuple

import resend
from resend.exceptions import ResendError

from app.config import settings

logger = logging.getLogger(__name__)


def _compose_subject(lead_type: str) -> str:
    return f"[Bold Crow MCP] New {lead_type} submission"


def _compose_body(lead_type: str, payload: Dict[str, Any]) -> str:
    return (
        f"Lead Type: {lead_type}\n\n"
        "Payload:\n"
        f"{json.dumps(payload, indent=2)}\n"
    )


def _reply_to_address(payload: Dict[str, Any]) -> Optional[str]:
    raw = payload.get("email")
    if isinstance(raw, str):
        cleaned = raw.strip()
        if cleaned and "@" in cleaned:
            return cleaned
    return None


def _envelope_from() -> str:
    return settings.smtp_from_email.strip()


def _recipient_list() -> List[str]:
    raw = settings.lead_notification_email.strip()
    if not raw:
        return []
    return [addr.strip() for addr in raw.split(",") if addr.strip()]


def _send_lead_via_resend(
    lead_type: str,
    payload: Dict[str, Any],
    recipients: List[str],
) -> Tuple[bool, str]:
    from_addr = settings.resend_from.strip()
    resend.api_key = settings.resend_api_key

    params: resend.Emails.SendParams = {
        "from": from_addr,
        "to": recipients,
        "subject": _compose_subject(lead_type),
        "text": _compose_body(lead_type, payload),
    }
    reply_to = _reply_to_address(payload)
    if reply_to:
        params["reply_to"] = reply_to

    try:
        result = resend.Emails.send(params)
        email_id = getattr(result, "id", None)
        if email_id is None and isinstance(result, dict):
            email_id = result.get("id")
        logger.info(
            "Resend lead email sent lead_type=%s resend_id=%s recipients=%s",
            lead_type,
            email_id,
            recipients,
        )
        return True, "Lead notification sent successfully."
    except ResendError as exc:
        logger.error(
            "Resend send failed lead_type=%s code=%s error_type=%s message=%s",
            lead_type,
            exc.code,
            exc.error_type,
            exc.message,
            exc_info=True,
        )
        return (
            False,
            "Lead captured, but the notification email could not be delivered.",
        )
    except Exception:
        logger.exception("Resend send failed unexpectedly lead_type=%s", lead_type)
        return (
            False,
            "Lead captured, but the notification email could not be delivered.",
        )


def _send_lead_via_smtp(
    lead_type: str,
    payload: Dict[str, Any],
    recipients: List[str],
) -> Tuple[bool, str]:
    msg = MIMEText(_compose_body(lead_type, payload), "plain", "utf-8")
    msg["Subject"] = _compose_subject(lead_type)
    msg["From"] = settings.smtp_from_email
    msg["To"] = ", ".join(recipients)
    reply_to = _reply_to_address(payload)
    if reply_to:
        msg["Reply-To"] = reply_to

    envelope_from = _envelope_from()
    try:
        context = ssl.create_default_context()
        if settings.use_ssl_transport:
            with smtplib.SMTP_SSL(
                settings.smtp_host,
                settings.smtp_port,
                timeout=30,
                context=context,
            ) as server:
                server.login(settings.smtp_username, settings.smtp_password)
                server.sendmail(
                    envelope_from,
                    recipients,
                    msg.as_string(),
                )
        else:
            with smtplib.SMTP(
                settings.smtp_host, settings.smtp_port, timeout=30
            ) as server:
                server.ehlo()
                server.starttls(context=context)
                server.ehlo()
                server.login(settings.smtp_username, settings.smtp_password)
                server.sendmail(
                    envelope_from,
                    recipients,
                    msg.as_string(),
                )
        logger.info(
            "Lead email sent lead_type=%s recipients=%s",
            lead_type,
            recipients,
        )
        return True, "Lead notification sent successfully."
    except Exception:
        logger.exception(
            "Lead email send failed lead_type=%s host=%s port=%s ssl=%s",
            lead_type,
            settings.smtp_host,
            settings.smtp_port,
            settings.use_ssl_transport,
        )
        return (
            False,
            "Lead captured, but the notification email could not be delivered.",
        )


def send_lead_email(lead_type: str, payload: Dict[str, Any]) -> Tuple[bool, str]:
    recipients = _recipient_list()
    if not recipients:
        logger.warning("Lead email skipped: LEAD_NOTIFICATION_EMAIL is empty")
        return (
            False,
            "Email notifications are not fully configured on this server.",
        )

    if settings.resend_enabled:
        return _send_lead_via_resend(lead_type, payload, recipients)

    if settings.smtp_enabled:
        return _send_lead_via_smtp(lead_type, payload, recipients)

    logger.warning(
        "Lead email skipped: configure Resend (RESEND_API_KEY, RESEND_FROM_EMAIL, "
        "LEAD_NOTIFICATION_EMAIL) or full SMTP plus LEAD_NOTIFICATION_EMAIL"
    )
    return (
        False,
        "Email notifications are not fully configured on this server.",
    )
