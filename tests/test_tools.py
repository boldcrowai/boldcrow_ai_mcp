from app.tools import (
    handle_get_agency_profile,
    handle_list_services,
    handle_recommend_service_path,
    handle_request_mcp_consultation,
    handle_request_website_audit,
    handle_submit_lead,
)


def test_get_agency_profile_contains_expected_keys():
    result = handle_get_agency_profile()
    assert result["company_name"] == "Bold Crow AI"
    assert "core_services" in result
    assert "contact_url" in result


def test_list_services_all_returns_non_empty():
    result = handle_list_services()
    assert "services" in result
    assert len(result["services"]) > 0


def test_recommend_service_path_returns_required_shape():
    result = handle_recommend_service_path(
        primary_goal="Improve AI visibility",
        current_problem="Not discoverable in AI tools",
        interested_in_mcp=True,
        timeline="immediate",
    )
    assert result["priority_level"] in {"low", "medium", "high"}
    assert isinstance(result["recommended_services"], list)
    assert "booking_url" in result


def test_request_website_audit_accepts_without_smtp():
    result = handle_request_website_audit(
        name="Dave",
        company="Bold Crow",
        email="[redacted-email]",
        website_url="https://boldcrow.ai",
        audit_type="full",
        notes="Please review",
    )
    assert result["status"] == "accepted"
    assert "message" in result
    assert "next_step" in result


def test_submit_lead_accepts_without_smtp():
    result = handle_submit_lead(
        name="Lead Name",
        email="lead@example.com",
        project_summary="Need help with AI strategy",
    )
    assert result["status"] == "accepted"
    assert "follow_up_path" in result


def test_request_mcp_consultation_accepts_without_smtp():
    result = handle_request_mcp_consultation(
        name="Jane",
        company="Acme",
        email="jane@acme.com",
        use_case="lead_generation",
    )
    assert result["status"] == "accepted"
    assert "recommended_next_step" in result
