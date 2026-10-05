# Other MCP clients

Any assistant or tool that can talk to a remote MCP server over Streamable HTTP and
send a custom header can connect to AveeCare.

| Setting | Value |
|---|---|
| URL | `https://app.aveecare.com/api/mcp` |
| Transport | Streamable HTTP |
| Authentication | Bearer token, sent as the header `Authorization: Bearer ak_...` |

Most clients take a JSON configuration shaped like this. The exact field names vary a
little between clients (`url` or `serverUrl`, `type` or `transport`), so check your
client's documentation:

```json
{
  "mcpServers": {
    "aveecare": {
      "type": "http",
      "url": "https://app.aveecare.com/api/mcp",
      "headers": {
        "Authorization": "Bearer ak_..."
      }
    }
  }
}
```

Prefer your client's way of reading a secret from an environment variable over a
literal key in the file.

## Clients that only run local programs

Some clients can only start local (stdio) servers. A bridge such as
[`mcp-remote`](https://www.npmjs.com/package/mcp-remote) can connect them to a remote
server:

```json
{
  "mcpServers": {
    "aveecare": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://app.aveecare.com/api/mcp",
        "--header",
        "Authorization:${AVEECARE_AUTH}"
      ],
      "env": {
        "AVEECARE_AUTH": "Bearer ak_..."
      }
    }
  }
}
```

`mcp-remote` is a third-party tool, not part of AveeCare. Review it before you run it
with a key that can read patient data.

## Not sure it is working?

You can check a key without an assistant by sending a request straight to the server:

```sh
curl -sS https://app.aveecare.com/api/mcp \
  -H "Authorization: Bearer $AVEECARE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'
```

A `401` means the key is wrong, revoked or expired. See [troubleshooting](troubleshooting.md).
