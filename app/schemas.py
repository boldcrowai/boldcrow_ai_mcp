from typing import Any, Dict, List


def get_service_catalog() -> List[Dict[str, Any]]:
    return [
        {
            "name": "AI Product Development",
            "category": "ai_products",
            "summary": "Design and ship AI-first products and assistants.",
            "best_for": ["new AI products", "internal AI copilots", "agent workflows"],
        },
        {
            "name": "Web Development",
            "category": "web_development",
            "summary": "Build high-conversion websites and web apps.",
            "best_for": ["redesigns", "conversion improvements", "custom builds"],
        },
        {
            "name": "SEO, GEO, and AEO",
            "category": "seo_geo_aeo",
            "summary": "Improve discoverability in search and AI answer engines.",
            "best_for": ["organic growth", "LLM discoverability", "content visibility"],
        },
        {
            "name": "Automation",
            "category": "automation",
            "summary": "Automate lead handling, operations, and reporting workflows.",
            "best_for": ["ops efficiency", "faster follow-up", "manual task reduction"],
        },
        {
            "name": "MCP Development",
            "category": "mcp_development",
            "summary": "Make businesses callable by conversational AI through MCP.",
            "best_for": ["AI visibility", "agent integrations", "structured AI access"],
        },
        {
            "name": "Strategy",
            "category": "strategy",
            "summary": "Prioritize roadmap and GTM around measurable outcomes.",
            "best_for": ["planning", "offer design", "technical prioritization"],
        },
    ]


def get_tool_schemas() -> Dict[str, Dict[str, Any]]:
    return {
        "get_agency_profile": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
        },
        "list_services": {
            "type": "object",
            "properties": {
                "category": {
                    "type": "string",
                    "enum": [
                        "all",
                        "ai_products",
                        "web_development",
                        "seo_geo_aeo",
                        "automation",
                        "mcp_development",
                        "strategy",
                    ],
                }
            },
            "additionalProperties": False,
        },
        "recommend_service_path": {
            "type": "object",
            "properties": {
                "business_name": {"type": "string"},
                "website_url": {"type": "string"},
                "industry": {"type": "string"},
                "primary_goal": {"type": "string"},
                "current_problem": {"type": "string"},
                "interested_in_mcp": {"type": "boolean"},
                "timeline": {
                    "type": "string",
                    "enum": ["immediate", "30_days", "90_days", "exploring"],
                },
                "budget_range": {
                    "type": "string",
                    "enum": [
                        "unknown",
                        "under_2500",
                        "2500_5000",
                        "5000_10000",
                        "10000_25000",
                        "25000_plus",
                    ],
                },
            },
            "required": ["primary_goal", "current_problem"],
            "additionalProperties": False,
        },
        "request_website_audit": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "company": {"type": "string"},
                "email": {"type": "string"},
                "website_url": {"type": "string"},
                "audit_type": {
                    "type": "string",
                    "enum": [
                        "website_performance",
                        "seo",
                        "geo_aeo",
                        "ai_readiness",
                        "full",
                    ],
                },
                "notes": {"type": "string"},
            },
            "required": ["name", "email", "website_url", "audit_type"],
            "additionalProperties": False,
        },
        "submit_lead": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "company": {"type": "string"},
                "email": {"type": "string"},
                "phone": {"type": "string"},
                "website_url": {"type": "string"},
                "service_interest": {"type": "array", "items": {"type": "string"}},
                "project_summary": {"type": "string"},
                "budget_range": {"type": "string"},
                "timeline": {"type": "string"},
            },
            "required": ["name", "email", "project_summary"],
            "additionalProperties": False,
        },
        "request_mcp_consultation": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "company": {"type": "string"},
                "email": {"type": "string"},
                "website_url": {"type": "string"},
                "business_type": {"type": "string"},
                "use_case": {
                    "type": "string",
                    "enum": [
                        "lead_generation",
                        "customer_support",
                        "service_discovery",
                        "internal_tools",
                        "partner_integrations",
                        "other",
                    ],
                },
                "needs_hosted_mcp": {"type": "boolean"},
                "needs_directory_submission": {"type": "boolean"},
                "notes": {"type": "string"},
            },
            "required": ["name", "company", "email", "use_case"],
            "additionalProperties": False,
        },
    }
