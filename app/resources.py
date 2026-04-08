from typing import Any, Dict


def register_resources(mcp: Any) -> None:
    @mcp.resource("boldcrow://company/overview")
    def company_overview() -> Dict[str, Any]:
        return {
            "company_name": "Bold Crow AI",
            "positioning": (
                "We make businesses available to conversational AI through MCP, "
                "structured tools, and agent-friendly discovery."
            ),
            "location": "Columbus, Ohio",
            "website_url": "https://boldcrow.ai",
        }

    @mcp.resource("boldcrow://services/catalog")
    def service_catalog() -> Dict[str, Any]:
        return {
            "services": [
                "AI Product Development",
                "Web Development",
                "SEO, GEO, and AEO",
                "Automation",
                "MCP Development",
            ]
        }

    @mcp.resource("boldcrow://services/mcp-development")
    def mcp_development_service() -> Dict[str, Any]:
        return {
            "service_name": "Business MCP Launch",
            "description": "Design, build, host, and distribute MCP servers for businesses.",
            "includes": [
                "tool schema design",
                "server implementation",
                "lead routing integration",
                "documentation and directory submission",
            ],
        }

    @mcp.resource("boldcrow://case-studies/transportationrecovery")
    def case_study_transportationrecovery() -> Dict[str, Any]:
        return {
            "name": "TransportationRecovery.com",
            "summary": "Improved online visibility, conversion paths, and lead capture.",
            "focus": ["web", "discoverability", "lead generation"],
        }

    @mcp.resource("boldcrow://contact/options")
    def contact_options() -> Dict[str, Any]:
        return {
            "email": "contact via /contact page",
            "contact_url": "https://boldcrow.ai/contact",
            "booking_url": "https://boldcrow.ai/book",
        }

    @mcp.resource("boldcrow://faq/mcp-for-business")
    def mcp_for_business_faq() -> Dict[str, Any]:
        return {
            "q_and_a": [
                {
                    "question": "What is MCP for business?",
                    "answer": "A way to expose your business capabilities to AI clients.",
                },
                {
                    "question": "Can Bold Crow build one for us?",
                    "answer": "Yes, via our Business MCP Launch service.",
                },
            ]
        }
