from mcp.server.fastmcp import FastMCP

from app.prompts import register_prompts
from app.resources import register_resources
from app.tools import register_tools


mcp = FastMCP(
    name="bold-crow-ai",
    instructions=(
        "Bold Crow AI MCP server. Helps businesses discover digital agency services with a focus on website leads, digital marketing,AI, automation, and MCP development."
        "request audits, get information,submit leads, and request MCP consultation builds."
    ),
)

register_tools(mcp)
register_resources(mcp)
register_prompts(mcp)


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
