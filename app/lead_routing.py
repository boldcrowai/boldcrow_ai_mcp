import json
import logging
import smtplib
import ssl
from email.mime.text import MIMEText
from typing import Any, Dict, List, Optional, Tuple

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


def send_lead_email(lead_type: str, payload: Dict[str, Any]) -> Tuple[bool, str]:
    if not settings.smtp_enabled:
        logger.warning(
            "Lead email skipped: SMTP not fully configured "
            "(need SMTP_HOST, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD, "
            "SMTP_FROM_EMAIL, LEAD_NOTIFICATION_EMAIL)"
        )
        return (
            False,
            "Email notifications are not fully configured on this server.",
        )

    recipients = _recipient_list()
    if not recipients:
        logger.warning("Lead email skipped: LEAD_NOTIFICATION_EMAIL is empty")
        return (
            False,
            "Email notifications are not fully configured on this server.",
        )

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
