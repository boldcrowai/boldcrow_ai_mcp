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
3. Copy `.env.example` to `.env` and add **Resend** or **SMTP** variables (see below).
4. Run server:
   - `python server.py`

## Environment Variables

### Resend (recommended on Railway)

HTTPS API email—avoids outbound SMTP blocks common on PaaS hosts.

- `RESEND_API_KEY` — API key from [Resend](https://resend.com) (starts with `re_`)
- `RESEND_FROM_EMAIL` — verified sender, e.g. `Bold Crow <leads@yourdomain.com>` (see setup below)
- `LEAD_NOTIFICATION_EMAIL` — where lead notifications are delivered (comma-separated allowed)

If `RESEND_API_KEY` is set and `RESEND_FROM_EMAIL` is empty, the server falls back to `SMTP_FROM_EMAIL` for the Resend `from` address (only if that address is allowed in your Resend domain).

### SMTP (alternative)

- `SMTP_HOST`
- `SMTP_PORT`
- `SMTP_USERNAME`
- `SMTP_PASSWORD`
- `SMTP_FROM_EMAIL`
- `LEAD_NOTIFICATION_EMAIL` (required with SMTP)
- `SMTP_USE_SSL` (optional; set to `true` for implicit TLS, e.g. port 465)

### Other

- `MCP_BASE_URL`
- `LOG_LEVEL` (optional)

## Resend setup (step by step)

1. Create an account at [resend.com](https://resend.com) and open the dashboard.
2. **Domains** → **Add domain** → add your domain (e.g. `boldcrow.ai`) and add the DNS records Resend shows (SPF/DKIM). Wait until the domain shows as verified.
3. **API Keys** → create a key with “Sending access” → copy it (starts with `re_`).
4. Choose a **From** address on that domain, e.g. `Bold Crow <leads@boldcrow.ai>`. It must match a verified domain in Resend.
5. In **Railway** → your MCP service → **Variables**, set:
   - `RESEND_API_KEY` = your key  
   - `RESEND_FROM_EMAIL` = your from line (must match Resend’s allowed senders)  
   - `LEAD_NOTIFICATION_EMAIL` = the inbox where you want lead alerts  
6. Redeploy, then trigger a test `request_mcp_consultation` or `request_website_audit` from Claude and confirm the message arrives.

**Testing without your own domain:** Resend’s test sender `onboarding@resend.dev` only works for limited testing; production should use a verified domain.

## Lead routing

When `RESEND_API_KEY`, `LEAD_NOTIFICATION_EMAIL`, and a non-empty **from** (`RESEND_FROM_EMAIL` or `SMTP_FROM_EMAIL`) are set, notifications go through **Resend’s API** (preferred).

Otherwise, if **all** SMTP variables and `LEAD_NOTIFICATION_EMAIL` are set, the server uses **SMTP**.

If neither path is configured, the lead tools still return `accepted` but no email is sent. Failed sends are logged (Railway: **Deployments → your service → Logs**).

**Note:** Lead payloads are not written to a database in this repo—notifications are email-only. If email fails, capture the conversation or check logs.

## Railway Deployment

- `railway.json` config is included.
- `Procfile` is included.
- Start command: `python server.py`

Set all environment variables in Railway before publishing the endpoint.

## Example positioning

Bold Crow messaging used in this implementation:

`We make businesses available to conversational AI through MCP, structured tools, and agent-friendly discovery.`
