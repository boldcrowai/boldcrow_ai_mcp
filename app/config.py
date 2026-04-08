import os
from dataclasses import dataclass


def _env_smtp_port() -> int:
    raw = os.getenv("SMTP_PORT", "587").strip()
    if not raw:
        return 587
    try:
        return int(raw)
    except ValueError:
        return 587


@dataclass(frozen=True)
class Settings:
    smtp_host: str = os.getenv("SMTP_HOST", "")
    smtp_port: int = _env_smtp_port()
    smtp_username: str = os.getenv("SMTP_USERNAME", "")
    smtp_password: str = os.getenv("SMTP_PASSWORD", "")
    smtp_from_email: str = os.getenv("SMTP_FROM_EMAIL", "")
    smtp_use_ssl: bool = os.getenv("SMTP_USE_SSL", "").strip().lower() in {
        "1",
        "true",
        "yes",
        "on",
    }
    lead_notification_email: str = os.getenv("LEAD_NOTIFICATION_EMAIL", "")
    resend_api_key: str = os.getenv("RESEND_API_KEY", "").strip()
    resend_from_email: str = os.getenv("RESEND_FROM_EMAIL", "").strip()
    mcp_base_url: str = os.getenv("MCP_BASE_URL", "http://localhost:8000")
    app_env: str = os.getenv("APP_ENV", "development")

    @property
    def resend_from(self) -> str:
        return self.resend_from_email or self.smtp_from_email

    @property
    def resend_enabled(self) -> bool:
        return bool(
            self.resend_api_key
            and self.lead_notification_email.strip()
            and self.resend_from.strip()
        )

    @property
    def smtp_enabled(self) -> bool:
        return all(
            [
                self.smtp_host,
                self.smtp_port,
                self.smtp_username,
                self.smtp_password,
                self.smtp_from_email,
                self.lead_notification_email.strip(),
            ]
        )

    @property
    def use_ssl_transport(self) -> bool:
        return self.smtp_use_ssl or self.smtp_port == 465


settings = Settings()
