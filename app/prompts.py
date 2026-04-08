from typing import Any


def register_prompts(mcp: Any) -> None:
    @mcp.prompt(
        name="find_best_bold_crow_service",
        description="Help a business determine the best Bold Crow service fit.",
    )
    def find_best_bold_crow_service(business_type: str, goal: str) -> str:
        return (
            "Assess this business and recommend the right Bold Crow service.\n"
            f"Business type: {business_type}\n"
            f"Goal/problem: {goal}\n"
            "Return a concise recommendation and next step."
        )

    @mcp.prompt(
        name="plan_an_mcp_for_my_business",
        description="Create a first-pass plan for MCP use in a company.",
    )
    def plan_an_mcp_for_my_business(company_name: str, use_case: str) -> str:
        return (
            "Create an MCP rollout outline for this company.\n"
            f"Company: {company_name}\n"
            f"Use case: {use_case}\n"
            "Include 4-6 tools, lead routing approach, and launch steps."
        )

    @mcp.prompt(
        name="evaluate_ai_discoverability",
        description="Assess how discoverable a business is through conversational AI.",
    )
    def evaluate_ai_discoverability(website_url: str) -> str:
        return (
            "Evaluate this website for AI discoverability readiness.\n"
            f"Website: {website_url}\n"
            "Highlight gaps in structured content, toolability, and conversion paths."
        )
