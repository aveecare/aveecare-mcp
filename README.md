# Connect AI assistants to AveeCare

[![CI](https://github.com/aveecare/aveecare-mcp/actions/workflows/ci.yml/badge.svg)](https://github.com/aveecare/aveecare-mcp/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Setup guides and ready-to-copy configuration for connecting AI assistants such as
Claude Code, Cursor, Windsurf and Codex to your agency's data in
[AveeCare](https://www.aveecare.com), home care software, through AveeCare's
[Model Context Protocol](https://modelcontextprotocol.io) (MCP) server.

Once connected, you can ask your assistant things like:

> Which caregivers have certifications expiring in the next 30 days?
>
> Summarize this week's missed visits.

and it answers from your live AveeCare data. See [example prompts](docs/example-prompts.md).

## Connection details

| | |
|---|---|
| **Server URL** | `https://app.aveecare.com/api/mcp` |
| **Transport** | Streamable HTTP |
| **Authentication** | `Authorization: Bearer ak_...` (an AveeCare API key) |
| **Rate limit** | 60 requests per minute per key, shared with the REST API |

## 1. Create an API key

In AveeCare open **Settings → API Keys** and create a key. Choose **Read-only**
(recommended for assistants) or **Read & write**. The key is shown once, so copy it
straight into a password manager or an environment variable. The same page has setup
snippets for each assistant, with your new key filled in.

A key acts as you: it sees and can change exactly what you can in AveeCare, in your
agency only. Read the [security notes](docs/security.md) before you connect an assistant.

## 2. Add the server to your assistant

Keep the key in an environment variable instead of pasting it into a config file:

```sh
export AVEECARE_API_KEY="ak_..."
```

| Assistant | Guide | Quick setup |
|---|---|---|
| Claude Code | [docs/claude-code.md](docs/claude-code.md) | `claude mcp add --transport http aveecare https://app.aveecare.com/api/mcp --header "Authorization: Bearer $AVEECARE_API_KEY"` |
| Codex (CLI and IDE) and ChatGPT | [docs/chatgpt-codex.md](docs/chatgpt-codex.md) | [`examples/codex.config.toml`](examples/codex.config.toml) |
| Cursor | [docs/cursor.md](docs/cursor.md) | [`examples/cursor.mcp.json`](examples/cursor.mcp.json) |
| Windsurf | [docs/windsurf.md](docs/windsurf.md) | [`examples/windsurf.mcp_config.json`](examples/windsurf.mcp_config.json) |
| Anything else | [docs/other-clients.md](docs/other-clients.md) | URL, transport and header above |

## 3. Ask a question

Start with something harmless, such as "Who am I connected to AveeCare as?" or
"List my five most recently added patients", then try the
[example prompts](docs/example-prompts.md).

## What your assistant can do

The assistant can look up and, with a read and write key, update information in these areas:

- **Patients:** profiles, contacts, allergies, medications, care goals and notes
- **Caregivers:** profiles, certifications and credentials, availability, specializations, applicants and notes
- **Scheduling:** visits, visit requests, open shifts and shift swaps
- **Care plans and documentation:** care plans, progress notes, incident reports, documented events and authorizations
- **Billing (read):** invoices, claims and payroll entries
- **Messaging:** conversations and messages
- **Agency:** offices, referral sources and alerts

A read-only key can only look things up. Anything the person who created the key
cannot see in AveeCare is not available to the assistant either.

## Prefer to write code?

The [REST API](https://www.aveecare.com/docs/api) and the official SDKs offer the
same data to your own programs, using the same API keys:

- [aveecare-openapi](https://github.com/aveecare/aveecare-openapi): the OpenAPI specification
- [aveecare-examples](https://github.com/aveecare/aveecare-examples): sample apps

## Official SDKs and tools

- [aveecare-node](https://github.com/aveecare/aveecare-node): Node.js and TypeScript
- [aveecare-python](https://github.com/aveecare/aveecare-python): Python
- [aveecare-rust](https://github.com/aveecare/aveecare-rust): Rust
- [aveecare-go](https://github.com/aveecare/aveecare-go): Go
- [aveecare-ruby](https://github.com/aveecare/aveecare-ruby): Ruby
- [aveecare-php](https://github.com/aveecare/aveecare-php): PHP
- [aveecare-java](https://github.com/aveecare/aveecare-java): Java and Kotlin
- [aveecare-dotnet](https://github.com/aveecare/aveecare-dotnet): .NET
- [aveecare-cli](https://github.com/aveecare/aveecare-cli): command line
- [aveecare-openapi](https://github.com/aveecare/aveecare-openapi): OpenAPI specification
- [aveecare-mcp](https://github.com/aveecare/aveecare-mcp): connect AI assistants
- [aveecare-examples](https://github.com/aveecare/aveecare-examples): sample apps

## Learn more

- [AveeCare](https://www.aveecare.com): home care software
- [API documentation](https://www.aveecare.com/docs/api)
- [Developers](https://www.aveecare.com/developers)
- [Partner Center](https://www.aveecare.com/partners): building an integration to offer other agencies?

## License

MIT. See [LICENSE](LICENSE).

---

Built by [AveeCare](https://www.aveecare.com) — home care software.

Suggested GitHub topics and keywords are listed in [`.github/TOPICS.md`](.github/TOPICS.md).
