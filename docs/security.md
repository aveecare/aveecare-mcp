# Security notes

An API key lets software read your agency's records, which include protected health
information. Please read this page before you connect an assistant.

## A key acts as you

- A key has the same access as the person who created it: it sees and can change
  exactly what that person can in AveeCare, in their agency only.
- Create the key from the account that has the least access that gets the job done.
  A scheduler's key can do less than an administrator's.
- Each key is **Read-only** or **Read & write**. A read-only key can look things up but
  cannot create, change or delete anything.

## Use a read-only key for assistants

Prefer **Read-only** keys for assistants. An assistant can misunderstand a request, and
text it reads (such as a patient note) can contain instructions it might follow. A
read-only key means the worst outcome is a wrong answer, not a changed schedule.

Use a **Read & write** key only for a specific task, and review each change the
assistant proposes before you approve it.

## Keep keys private

- Never paste a key into a shared prompt, a chat that other people can read, a ticket,
  an email, a screenshot or a public repository.
- Put the key in an environment variable or a password manager. The configuration
  examples here read it from `AVEECARE_API_KEY` so the key is not stored in the file.
- Do not commit assistant configuration files that contain a literal key. This
  repository's `.gitignore` excludes `.env` files, and you should do the same in your
  own projects.
- Give each assistant or person their own key with a clear label (for example
  "Claude Code - front desk laptop"), so you can revoke one without disturbing the
  others.
- A key is shown once when you create it. If you lose it, create a new one.

## Revoking a key

If a key may have been exposed, or you no longer use the assistant:

1. Open **Settings → API Keys** in AveeCare.
2. Find the key by its label. The page shows when it was last used.
3. Revoke it.

A revoked key stops working within seconds. Create a replacement if you still need
access, and update the environment variable that held the old one.

## What the assistant can send elsewhere

Your assistant sends what it reads from AveeCare to the company that runs it, under
that company's terms. Before you connect an assistant, make sure your agency's
policies and its agreement with that provider cover protected health information.
When in doubt, ask only questions that do not need patient names.

## Limits

Each key may make 60 requests a minute, shared between the assistant and any other
program using the same key. After repeated failed sign-in attempts from one network,
further requests from it are blocked for a while.

## Reporting a problem

Email **security@aveecare.com**. See [SECURITY.md](../SECURITY.md).
