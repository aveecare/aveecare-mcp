# Troubleshooting

## The assistant cannot connect, or says it is unauthorized (401)

- The key may be mistyped, truncated, expired or revoked. Keys look like
  `ak_` followed by letters and digits. Check **Settings → API Keys** to see whether
  the key is still active, and create a new one if not.
- The header must be exactly `Authorization: Bearer ak_...`, with the word `Bearer`
  and one space before the key.
- If you used an environment variable, make sure it is set in the program that starts
  the assistant, not only in a different terminal window. Echo it to check:
  `echo $AVEECARE_API_KEY`.
- Several failed attempts from one network block further requests from it for a
  while. Fix the key, then wait a few minutes before retrying.

AveeCare gives the same answer for every kind of key problem on purpose, so the error
cannot tell you which one it was.

## "This API key is read-only"

You asked the assistant to create, change or delete something with a read-only key.
Either do it in AveeCare yourself, or create a **Read & write** key for that task.
A read-only key does not show change tools to the assistant at all.

## Too many requests (429)

Each key may make 60 requests a minute, shared with any other program using the same
key. Wait a minute, or narrow the question (a shorter date range, one patient
instead of all of them).

## An answer is missing records

- The assistant only sees what the person who created the key can see.
- Large lists are returned in pages, and an assistant may stop after the first few.
  Ask for "all of them" or narrow the window.
- Check the record in AveeCare. If AveeCare shows something the assistant does not,
  tell it which record, and ask it to look again.

## The server does not appear in my client

- Restart the client after editing its configuration.
- Check the JSON for a missing comma or bracket. Each file in
  [`examples/`](../examples) is valid and can be copied as is.
- Make sure the URL is exactly `https://app.aveecare.com/api/mcp`, with no trailing
  slash and no extra path.

## Still stuck?

Open an [issue](https://github.com/aveecare/aveecare-mcp/issues) without including your
key or any patient information, or contact AveeCare support from your account.
