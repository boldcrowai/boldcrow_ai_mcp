# Bold Crow MCP Server

Production-ready V1 MCP server for Bold Crow AI.

This server does two jobs:
- helps prospects discover and contact Bold Crow AI
- demonstrates the exact MCP service Bold Crow can build for clients

## V1 Tools

- `get_agency_profile`
- `list_services`
- `recommend_service_path`
- `request_website_audit`
- `submit_lead`
- `request_mcp_consultation`

## Resources

- `boldcrow://company/overview`
- `boldcrow://services/catalog`
- `boldcrow://services/mcp-development`
- `boldcrow://case-studies/transportationrecovery`
- `boldcrow://contact/options`
- `boldcrow://faq/mcp-for-business`

## Prompts

- `find_best_bold_crow_service`
- `plan_an_mcp_for_my_business`
- `evaluate_ai_discoverability`

## Local Setup

1. Create and activate a Python virtual environment.
2. Install dependencies:
   - `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and fill SMTP values.
4. Run server:
   - `python server.py`

## Environment Variables

- `SMTP_HOST`
- `SMTP_PORT`
- `SMTP_USERNAME`
- `SMTP_PASSWORD`
- `SMTP_FROM_EMAIL`
- `LEAD_NOTIFICATION_EMAIL` (set to `[redacted-email]`)
- `MCP_BASE_URL`

## Lead Routing

Lead-capture tools send notifications to `[redacted-email]` through SMTP.
If SMTP is not configured yet, the tools still accept submissions and return
a fallback message so no lead interaction is dropped at runtime.

## Railway Deployment

- `railway.json` config is included.
- `Procfile` is included.
- Start command: `python server.py`

Set all environment variables in Railway before publishing the endpoint.

## Example Positioning

Bold Crow messaging used in this implementation:

`We make businesses available to conversational AI through MCP, structured tools, and agent-friendly discovery.`
# boldcrow_ai_mcp
