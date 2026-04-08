import os

import uvicorn
from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings

from app.prompts import register_prompts
from app.resources import register_resources
from app.tools import register_tools


mcp_port = int(os.getenv("PORT", "8000"))
railway_host = os.getenv("RAILWAY_PUBLIC_DOMAIN", "").strip()
allowed_hosts = ["localhost:*", "127.0.0.1:*", "0.0.0.0:*"]
if railway_host:
    allowed_hosts.append(f"{railway_host}:*")
    allowed_hosts.append(railway_host)

mcp = FastMCP(
    name="bold-crow-ai",
    instructions=(
        "Bold Crow AI MCP server. Helps businesses discover digital agency services with a focus on website leads, digital marketing,AI, automation, and MCP development."
        "request audits, get information,submit leads, and request MCP consultation builds."
    ),
    host="0.0.0.0",
    port=mcp_port,
    transport_security=TransportSecuritySettings(
        enable_dns_rebinding_protection=True,
        allowed_hosts=allowed_hosts,
        allowed_origins=[],
    ),
)

register_tools(mcp)
register_resources(mcp)
register_prompts(mcp)
app = mcp.streamable_http_app()


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=mcp_port,
    )
