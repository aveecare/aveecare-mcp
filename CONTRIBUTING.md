# Contributing to aveecare-mcp

Thanks for helping improve the AveeCare assistant guides.

This repository holds documentation and configuration examples for connecting AI
assistants to AveeCare. There is no code to build.

## What is welcome

- Setup guides for more assistants and editors, and corrections when an assistant
  changes how it configures MCP servers.
- Better example prompts for home care agencies.
- Fixes to wording, links and the example configurations.

## Ground rules

- Never include a real API key, patient name or other agency data in an example,
  issue or pull request. Use `ak_...` placeholders and made-up names.
- Prefer configuration that reads the key from an environment variable over a
  literal key.
- Describe what the assistant can do by area (patients, caregivers, scheduling, and so
  on). Do not add tool-by-tool lists.

## Checking your change

```sh
python scripts/check_configs.py    # example configs parse and hold no real key (Python 3.11+)
```

Open an issue first for anything larger than a small fix, and add a line to
`CHANGELOG.md` under "Unreleased".

By contributing you agree that your contributions are licensed under the MIT
License, and you agree to follow our [Code of Conduct](CODE_OF_CONDUCT.md).

Security issues: please follow [SECURITY.md](SECURITY.md) instead of opening a
public issue.
