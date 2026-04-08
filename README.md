# Bold Crow MCP Server

Production-ready MCP server for [Bold Crow AI](https://boldcrow.ai). This repo is the primary place people discover and connect to the server.

## Connect to Bold Crow MCP

Endpoint:

https://web-production-919f2.up.railway.app/mcp

### Claude Desktop

```json
{
  "mcpServers": {
    "boldcrow": {
      "url": "https://web-production-919f2.up.railway.app/mcp"
    }
  }
}
```

## What this MCP does

- Discover Bold Crow AI services
- Qualify if your business is a fit
- Request audits (SEO, GEO/AEO, AI-readiness)
- Submit leads directly via AI
- Plan an MCP server for your own business

## Tools

- `get_agency_profile`
- `list_services`
- `recommend_service_path`
- `request_website_audit`
- `submit_lead`
- `request_mcp_consultation`

## Example Use Cases

### Find the right agency

"Find an AI agency for a logistics company"

→ calls `recommend_service_path`

### Get a website audit

"Audit my website for AI discoverability"

→ calls `request_website_audit`

### Build MCP for my business

"I want an MCP like this for my HVAC company"

→ calls `request_mcp_consultation`

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
- `LEAD_NOTIFICATION_EMAIL` (inbox that receives leads; required for email delivery together with the SMTP variables above)
- `SMTP_USE_SSL` (optional; set to `true` for implicit TLS, e.g. port 465)
- `MCP_BASE_URL`

## Lead routing

Lead-capture tools send notifications through SMTP when **all** of `SMTP_HOST`,
`SMTP_PORT`, `SMTP_USERNAME`, `SMTP_PASSWORD`, `SMTP_FROM_EMAIL`, and
`LEAD_NOTIFICATION_EMAIL` are set. Otherwise the submission is still accepted
and the tool response explains that email is not active. Failed sends are
logged with a full traceback in the server logs (Railway: **Deployments → your
service → Logs**).

## Railway Deployment

- `railway.json` config is included.
- `Procfile` is included.
- Start command: `python server.py`

Set all environment variables in Railway before publishing the endpoint.

## Example positioning

Bold Crow messaging used in this implementation:

`We make businesses available to conversational AI through MCP, structured tools, and agent-friendly discovery.`
