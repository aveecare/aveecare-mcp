# Windsurf

Connect [Windsurf](https://windsurf.com) to AveeCare.

## Before you start

- An AveeCare API key from **Settings → API Keys** (read-only is recommended).
- The key in an environment variable, set before you start Windsurf:

  ```sh
  export AVEECARE_API_KEY="ak_..."
  ```

## Add the server

Open Windsurf's MCP settings (Cascade panel, **MCP servers**, then **View raw config**)
to edit its `mcp_config.json`, and add AveeCare
([`examples/windsurf.mcp_config.json`](../examples/windsurf.mcp_config.json)):

```json
{
  "mcpServers": {
    "aveecare": {
      "serverUrl": "https://app.aveecare.com/api/mcp",
      "headers": {
        "Authorization": "Bearer ${env:AVEECARE_API_KEY}"
      }
    }
  }
}
```

Windsurf fills in `${env:AVEECARE_API_KEY}` from your environment, so the key is not
stored in the file. If the file already lists other servers, add `aveecare` next to
them inside `mcpServers`. Refresh the MCP server list afterwards.

## Check it works

`aveecare` should appear in the MCP server list with its tools. Then ask Cascade:

> Which AveeCare account am I connected to, and can I make changes?

## Troubleshooting

See [troubleshooting](troubleshooting.md).

Next: [example prompts](example-prompts.md) and [security notes](security.md).
