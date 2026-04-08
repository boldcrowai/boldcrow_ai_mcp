from typing import Any, Dict, List, Optional

from app.lead_routing import send_lead_email
from app.schemas import get_service_catalog


def _recommend_priority(timeline: str, budget_range: str) -> str:
    if timeline == "immediate":
        return "high"
    if budget_range in {"10000_25000", "25000_plus"}:
        return "high"
    if timeline in {"30_days", "90_days"}:
        return "medium"
    return "low"


def _recommend_services(
    primary_goal: str, current_problem: str, interested_in_mcp: bool
) -> List[str]:
    goal = (primary_goal + " " + current_problem).lower()
    services: List[str] = []

    if "website" in goal or "conversion" in goal:
        services.append("Web Development")
    if "seo" in goal or "geo" in goal or "aeo" in goal or "discover" in goal:
        services.append("SEO, GEO, and AEO")
    if "automation" in goal or "workflow" in goal or "ops" in goal:
        services.append("Automation")
    if "ai" in goal or "assistant" in goal or "agent" in goal:
        services.append("AI Product Development")
    if interested_in_mcp or "mcp" in goal:
        services.append("MCP Development")

    if not services:
        services.append("Strategy")

    return sorted(set(services))


def handle_get_agency_profile() -> Dict[str, Any]:
    return {
        "company_name": "Bold Crow AI",
        "tagline": "AI-first agency for conversational discoverability",
        "location": "Columbus, Ohio",
        "summary": (
            "Bold Crow AI helps businesses become callable and discoverable "
            "through conversational AI, structured tools, and MCP."
        ),
        "core_services": [
            "AI Product Development",
            "Web Development",
            "SEO, GEO, and AEO",
            "Automation",
            "MCP Development",
        ],
        "ideal_clients": [
            "service businesses",
            "local businesses",
            "growth-stage companies",
            "teams adopting AI workflows",
        ],
        "website_url": "https://boldcrow.ai",
        "contact_url": "https://boldcrow.ai/contact",
    }


def handle_list_services(category: str = "all") -> Dict[str, Any]:
    services = get_service_catalog()
    if category == "all":
        return {"services": services}
    return {"services": [service for service in services if service["category"] == category]}


def handle_recommend_service_path(
    primary_goal: str,
    current_problem: str,
    business_name: str = "",
    website_url: str = "",
    industry: str = "",
    interested_in_mcp: bool = False,
    timeline: str = "exploring",
    budget_range: str = "unknown",
) -> Dict[str, Any]:
    recommended_services = _recommend_services(
        primary_goal, current_problem, interested_in_mcp
    )
    priority_level = _recommend_priority(timeline, budget_range)
    fit_summary = (
        f"{business_name or 'This business'} is a fit for Bold Crow AI based on "
        f"goal '{primary_goal}' and current challenge '{current_problem}'."
    )
    return {
        "fit_summary": fit_summary,
        "recommended_services": recommended_services,
        "recommended_next_step": "Book a strategy call and share your current funnel.",
        "priority_level": priority_level,
        "booking_url": "https://boldcrow.ai/book",
        "context": {
            "industry": industry,
            "website_url": website_url,
            "timeline": timeline,
            "budget_range": budget_range,
        },
    }


def _lead_acknowledgement(send_ok: bool, msg: str, next_step: str) -> Dict[str, Any]:
    return {
        "status": "accepted",
        "message": msg if send_ok else f"{msg} We will still follow up.",
        "next_step": next_step,
    }


def handle_request_website_audit(**payload: Any) -> Dict[str, Any]:
    send_ok, msg = send_lead_email("website_audit", payload)
    response = _lead_acknowledgement(
        send_ok,
        msg,
        "Our team will review your site and share proposed action steps.",
    )
    return response


def handle_submit_lead(**payload: Any) -> Dict[str, Any]:
    send_ok, msg = send_lead_email("general_lead", payload)
    return {
        "status": "accepted",
        "message": msg if send_ok else f"{msg} We will still follow up.",
        "follow_up_path": "You will receive outreach from Bold Crow AI soon.",
    }


def handle_request_mcp_consultation(**payload: Any) -> Dict[str, Any]:
    send_ok, msg = send_lead_email("mcp_consultation", payload)
    return {
        "status": "accepted",
        "message": msg if send_ok else f"{msg} We will still follow up.",
        "recommended_next_step": (
            "Book an MCP consultation call to map your business tools and rollout."
        ),
    }


def register_tools(mcp: Any) -> None:
    @mcp.tool(
        name="get_agency_profile",
        description="Returns Bold Crow AI company overview and service categories.",
    )
    def get_agency_profile() -> Dict[str, Any]:
        return handle_get_agency_profile()

    @mcp.tool(
        name="list_services",
        description="Returns services offered by Bold Crow AI, optionally by category.",
    )
    def list_services(category: str = "all") -> Dict[str, Any]:
        return handle_list_services(category)

    @mcp.tool(
        name="recommend_service_path",
        description="Recommends the best service path based on business details.",
    )
    def recommend_service_path(
        primary_goal: str,
        current_problem: str,
        business_name: str = "",
        website_url: str = "",
        industry: str = "",
        interested_in_mcp: bool = False,
        timeline: str = "exploring",
        budget_range: str = "unknown",
    ) -> Dict[str, Any]:
        return handle_recommend_service_path(
            primary_goal=primary_goal,
            current_problem=current_problem,
            business_name=business_name,
            website_url=website_url,
            industry=industry,
            interested_in_mcp=interested_in_mcp,
            timeline=timeline,
            budget_range=budget_range,
        )

    @mcp.tool(
        name="request_website_audit",
        description="Captures a website or AI-readiness audit request.",
    )
    def request_website_audit(
        name: str,
        email: str,
        website_url: str,
        audit_type: str,
        company: str = "",
        notes: str = "",
    ) -> Dict[str, Any]:
        return handle_request_website_audit(
            name=name,
            company=company,
            email=email,
            website_url=website_url,
            audit_type=audit_type,
            notes=notes,
        )

    @mcp.tool(
        name="submit_lead",
        description="Submits a general lead to Bold Crow AI for follow-up.",
    )
    def submit_lead(
        name: str,
        email: str,
        project_summary: str,
        company: str = "",
        phone: str = "",
        website_url: str = "",
        service_interest: Optional[List[str]] = None,
        budget_range: str = "unknown",
        timeline: str = "exploring",
    ) -> Dict[str, Any]:
        return handle_submit_lead(
            name=name,
            company=company,
            email=email,
            phone=phone,
            website_url=website_url,
            service_interest=service_interest or [],
            project_summary=project_summary,
            budget_range=budget_range,
            timeline=timeline,
        )

    @mcp.tool(
        name="request_mcp_consultation",
        description="Captures business inquiry to build MCP for their company.",
    )
    def request_mcp_consultation(
        name: str,
        company: str,
        email: str,
        use_case: str,
        website_url: str = "",
        business_type: str = "",
        needs_hosted_mcp: bool = True,
        needs_directory_submission: bool = True,
        notes: str = "",
    ) -> Dict[str, Any]:
        return handle_request_mcp_consultation(
            name=name,
            company=company,
            email=email,
            website_url=website_url,
            business_type=business_type,
            use_case=use_case,
            needs_hosted_mcp=needs_hosted_mcp,
            needs_directory_submission=needs_directory_submission,
            notes=notes,
        )
