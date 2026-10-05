# Claude Code

Connect [Claude Code](https://claude.com/claude-code) to AveeCare.

## Before you start

- An AveeCare API key from **Settings → API Keys** (read-only is recommended).
- The key in an environment variable, so it never lands in a shell history or a file you share:

  ```sh
  export AVEECARE_API_KEY="ak_..."
  ```

## Add the server

```sh
claude mcp add --transport http aveecare https://app.aveecare.com/api/mcp \
  --header "Authorization: Bearer $AVEECARE_API_KEY"
```

Your shell expands `$AVEECARE_API_KEY` before Claude Code stores the header, so the
key itself is saved in Claude Code's configuration for your user. Treat that file as
a secret.

By default the server is available to you in the current project only. Add
`--scope user` to make it available in every project. Avoid `--scope project` for a
real key: it writes `.mcp.json` into the repository, where it can be committed by
accident. If you do share a project file, keep the key out of it with an environment
variable reference (see below).

### Keeping the key out of the file

Claude Code expands `${VAR}` in `.mcp.json`, so a project file can hold no secret at all.
[`examples/claude-code.mcp.json`](../examples/claude-code.mcp.json):

```json
{
  "mcpServers": {
    "aveecare": {
      "type": "http",
      "url": "https://app.aveecare.com/api/mcp",
      "headers": {
        "Authorization": "Bearer ${AVEECARE_API_KEY}"
      }
    }
  }
}
```

Each teammate sets `AVEECARE_API_KEY` to their own key.

## Check it works

```sh
claude mcp list
```

`aveecare` should show as connected. Then start `claude` and ask:

> Which AveeCare account am I connected to, and can I make changes?

## Remove it

```sh
claude mcp remove aveecare
```

Then [revoke the key](security.md#revoking-a-key) in AveeCare if you no longer need it.

## Troubleshooting

See [troubleshooting](troubleshooting.md).

Next: [example prompts](example-prompts.md) and [security notes](security.md).
