# ChatGPT and Codex

## Codex (CLI, desktop app and IDE extension)

Codex reads MCP servers from `~/.codex/config.toml`. Put your key in an environment
variable and let Codex read it from there:

```sh
export AVEECARE_API_KEY="ak_..."
```

Add this to `~/.codex/config.toml`
([`examples/codex.config.toml`](../examples/codex.config.toml)):

```toml
[mcp_servers.aveecare]
url = "https://app.aveecare.com/api/mcp"
bearer_token_env_var = "AVEECARE_API_KEY"
```

Restart Codex so it picks up the new server, and make sure the environment variable
is set in the shell or app environment that launches it. Codex sends the key as
`Authorization: Bearer <key>`.

## ChatGPT

AveeCare's server authenticates with an API key sent as a bearer token. It does not
offer OAuth sign-in.

In versions of ChatGPT whose MCP server settings let you enter a URL and an
authorization header:

1. Open **Settings** and find the **MCP Servers** (or custom connector) settings. Some
   plans keep this behind **Developer mode**.
2. Click **Add** and set the URL to `https://app.aveecare.com/api/mcp`.
3. Set the transport to **Streamable HTTP**.
4. Add an `Authorization` header with the value `Bearer ak_...` (your key).

If your ChatGPT version only offers OAuth or no authentication for custom connectors,
it cannot connect to AveeCare. Use Codex, [Claude Code](claude-code.md),
[Cursor](cursor.md) or [Windsurf](windsurf.md) instead. ChatGPT runs the connection
from OpenAI's servers, so as with any assistant, only use a
[read-only key](security.md) there unless you need it to make changes.

## Check it works

Ask:

> Which AveeCare account am I connected to, and can I make changes?

## Troubleshooting

See [troubleshooting](troubleshooting.md).

Next: [example prompts](example-prompts.md) and [security notes](security.md).
