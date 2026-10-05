# Cursor

Connect [Cursor](https://cursor.com) to AveeCare.

## Before you start

- An AveeCare API key from **Settings → API Keys** (read-only is recommended).
- The key in an environment variable, set before you start Cursor:

  ```sh
  export AVEECARE_API_KEY="ak_..."
  ```

## Add the server

Create `~/.cursor/mcp.json` to make AveeCare available in every project, or
`.cursor/mcp.json` inside one project
([`examples/cursor.mcp.json`](../examples/cursor.mcp.json)):

```json
{
  "mcpServers": {
    "aveecare": {
      "url": "https://app.aveecare.com/api/mcp",
      "headers": {
        "Authorization": "Bearer ${env:AVEECARE_API_KEY}"
      }
    }
  }
}
```

Cursor fills in `${env:AVEECARE_API_KEY}` from your environment, so the key is not
stored in the file. If the file already has other servers, add `aveecare` next to them
inside `mcpServers`.

Do not commit a `.cursor/mcp.json` that contains a literal key. Using the
`${env:...}` form above keeps the file safe to share.

## Check it works

Open **Settings → MCP** (or **Tools & MCP**) in Cursor: `aveecare` should show as
enabled with its tools listed. Then ask in chat:

> Which AveeCare account am I connected to, and can I make changes?

## Troubleshooting

See [troubleshooting](troubleshooting.md).

Next: [example prompts](example-prompts.md) and [security notes](security.md).
