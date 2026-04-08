import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    smtp_host: str = os.getenv("SMTP_HOST", "")
    smtp_port: int = int(os.getenv("SMTP_PORT", "587"))
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
    mcp_base_url: str = os.getenv("MCP_BASE_URL", "http://localhost:8000")
    app_env: str = os.getenv("APP_ENV", "development")

    @property
    def smtp_enabled(self) -> bool:
        return all(
            [
                self.smtp_host,
                self.smtp_port,
                self.smtp_username,
                self.smtp_password,
                self.smtp_from_email,
            ]
        )

    @property
    def use_ssl_transport(self) -> bool:
        return self.smtp_use_ssl or self.smtp_port == 465


settings = Settings()
