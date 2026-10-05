# Security Policy

## Reporting a vulnerability

Please report security issues privately to **security@aveecare.com**. Do not
open a public GitHub issue, pull request or discussion for a vulnerability.

Include what you can of the following:

- the affected document or configuration (aveecare-mcp)
- a description of the issue and its impact
- steps to reproduce or a proof of concept

We will acknowledge your report, keep you informed while we investigate, and
credit you in the release notes if you would like.

## Scope

This repository contains documentation and configuration examples. Issues in the AveeCare API,
the AveeCare MCP server or the application itself are also welcome at the same address.

## Handling API keys

AveeCare API keys grant access to agency data, including protected health
information. Prefer read-only keys for AI assistants, keep keys in environment
variables or a password manager, and never put a key in a shared prompt, a screenshot
or a public repository. If a key is exposed, revoke it in AveeCare (Settings, API Keys)
right away and create a new one. See [docs/security.md](docs/security.md).

## Supported versions

Security fixes are released for the latest minor version.
