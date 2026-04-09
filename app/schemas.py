from typing import Any, Dict, List


def get_service_catalog() -> List[Dict[str, Any]]:
    return [
        {
            "name": "Web Design & UX Services",
            "category": "web_design_ux",
            "summary": (
                "Custom web design for modern B2B, B2C, and eCommerce websites. "
                "Clear plans, clean UI, faster sites."
            ),
            "details": [
                "User-centered design process",
                "On-brand design",
                "WCAG 2.2 AA accessibility compliance",
                "Working prototypes ready for development",
            ],
        },
        {
            "name": "Web App & API Development",
            "category": "web_app_api_development",
            "summary": (
                "Directories, databases, tools, and workflows that save time. "
                "Built simply and with a purpose."
            ),
            "details": [
                "Fast prototyping & iteration",
                "RESTful API development",
                "Database design & optimization",
                "Authentication & authorization",
            ],
        },
        {
            "name": "Custom WordPress Theme Development",
            "category": "wordpress_theme_development",
            "summary": (
                "No bloat. Custom field blocks, custom design, and strong "
                "performance targets."
            ),
            "details": [
                "Code-first workflow",
                "Core Web Vitals optimization",
                "No page builders (Gutenberg-native)",
                "Custom block development",
            ],
        },
        {
            "name": "AI-Powered Systems",
            "category": "ai_powered_systems",
            "summary": (
                "Add search, summaries, conversations, and automations that help "
                "users get what they need, often without leaving the page."
            ),
            "details": [
                "Retrieval Augmented Generation (RAG)",
                "Semantic search & embeddings",
                "Structured outputs & function calling",
                "Agent-ready APIs for zero-click task completion",
            ],
        },
        {
            "name": "Social Media Content",
            "category": "social_media_content",
            "summary": (
                "AI-generated social content that's on-brand, engaging, and ready "
                "to post. Visual and written content at scale."
            ),
            "details": [
                "AI-generated images and graphics",
                "Animated video and motion graphics",
                "On-brand visual asset generation",
                "Automated copywriting and captions",
            ],
        },
        {
            "name": "Performance, Hosting, & Maintenance",
            "category": "performance_hosting_maintenance",
            "summary": "Core web vitals, hosting, backups, updates, and monitoring.",
            "details": [
                "Core web vitals monitoring",
                "Regular security updates",
                "Automated backups",
                "Uptime monitoring",
            ],
        },
        {
            "name": "SEO + GEO + AEO",
            "category": "seo_geo_aeo",
            "summary": (
                "Traditional SEO plus optimization for AI search, LLMs, Google AI "
                "Overviews, and agent-ready content."
            ),
            "details": [
                "Schema markup implementation (JSON-LD)",
                "On-page SEO optimization",
                "AI-readable content structure",
                "Generative Engine Optimization (GEO)",
            ],
        },
        {
            "name": "Branding & Identity",
            "category": "branding_identity",
            "summary": (
                "Logos, brand assets, and identity systems powered by AI and "
                "refined by design experts."
            ),
            "details": [
                "AI-powered logo generation",
                "Custom brand identity systems",
                "Rapid iteration and refinement",
                "Complete brand asset library",
            ],
        },
        {
            "name": "PPC Campaign Management",
            "category": "ppc_campaign_management",
            "summary": (
                "Smarter bidding, dynamic creatives, hyper-personalized landing "
                "pages, and optimization for AI Search results."
            ),
            "details": [
                "Hyper-personalized landing page experiences",
                "Dynamic ad creative generation & assembly",
                "Predictive analytics & trend forecasting",
                "Automated A/B testing & performance insights",
            ],
        },
        {
            "name": "MCP Development",
            "category": "mcp_development",
            "summary": "Make businesses callable by conversational AI through MCP. MCP stands for Model Context Protocol and allows businesses to execute structured tools and functions through AI.",
            "details": [
                "Hosted MCP server implementation",
                "Tool and resource design",
                "Agent integrations and directory submission",
                "Structured AI access for business systems",
            ],
            "best_for": [
                "AI visibility",
                "agent integrations",
                "structured AI access",
            ],
        },
        {
            "name": "Consulting & Audits",
            "category": "consulting_audits",
            "summary": "Clear findings and suggestions in 1-2 weeks.",
            "details": [
                "Performance audit (Lighthouse)",
                "Accessibility review (WCAG 2.2)",
                "SEO & schema validation",
                "Process & pipeline automations",
            ],
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
                        "web_design_ux",
                        "web_app_api_development",
                        "wordpress_theme_development",
                        "ai_powered_systems",
                        "social_media_content",
                        "performance_hosting_maintenance",
                        "seo_geo_aeo",
                        "branding_identity",
                        "ppc_campaign_management",
                        "mcp_development",
                        "consulting_audits",
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
