import json
import smtplib
from email.mime.text import MIMEText
from typing import Any, Dict, Tuple

from app.config import settings


def _compose_subject(lead_type: str) -> str:
    return f"[Bold Crow MCP] New {lead_type} submission"


def _compose_body(lead_type: str, payload: Dict[str, Any]) -> str:
    return (
        f"Lead Type: {lead_type}\n\n"
        "Payload:\n"
        f"{json.dumps(payload, indent=2)}\n"
    )


def send_lead_email(lead_type: str, payload: Dict[str, Any]) -> Tuple[bool, str]:
    if not settings.smtp_enabled:
        return False, "SMTP not configured. Lead captured in response only."

    msg = MIMEText(_compose_body(lead_type, payload), "plain", "utf-8")
    msg["Subject"] = _compose_subject(lead_type)
    msg["From"] = settings.smtp_from_email
    msg["To"] = settings.lead_notification_email

    try:
        if settings.use_ssl_transport:
            with smtplib.SMTP_SSL(
                settings.smtp_host, settings.smtp_port, timeout=15
            ) as server:
                server.login(settings.smtp_username, settings.smtp_password)
                server.sendmail(
                    settings.smtp_from_email,
                    [settings.lead_notification_email],
                    msg.as_string(),
                )
        else:
            with smtplib.SMTP(settings.smtp_host, settings.smtp_port, timeout=15) as server:
                server.starttls()
                server.login(settings.smtp_username, settings.smtp_password)
                server.sendmail(
                    settings.smtp_from_email,
                    [settings.lead_notification_email],
                    msg.as_string(),
                )
        return True, "Lead notification sent successfully."
    except Exception as exc:
        return False, f"Lead captured but email send failed: {exc}"
