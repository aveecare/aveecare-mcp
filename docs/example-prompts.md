# Example prompts for home care agencies

Prompts that work well once your assistant is [connected](../README.md). A read-only
key is enough for every prompt in the first four sections; the last section needs a
read and write key.

Assistants do better with a clear time window and a clear output, so say "next 30
days" rather than "soon", and ask for a table, a list or a short summary.

## Caregivers and credentials

- Which caregivers have certifications expiring in the next 30 days? Show the caregiver, the certification and the expiry date, soonest first.
- List caregivers whose state license has already expired.
- Which active caregivers have no CPR certification on file?
- Who are my caregivers who speak Spanish and are marked active?
- Which caregivers have not had a visit in the last 60 days?

## Scheduling and visits

- Summarize this week's missed visits. Group them by patient and note which caregiver was scheduled.
- Which visits tomorrow have no caregiver assigned?
- Show every visit scheduled for Margaret Alvarez next week.
- How many hours was each caregiver scheduled for last week?
- Which open shifts are still unfilled this week?
- Which visits last week ran late or were left incomplete?

## Patients and care plans

- List my active patients with a fall risk flag.
- Which patients have a prior authorization that expires in the next 30 days?
- Which patients were added in the last 14 days?
- Summarize the latest progress notes for Margaret Alvarez in three sentences.

## Incidents, billing and messages

- List incident reports opened this month that are still unresolved, with severity and patient.
- Which incident reports need a follow-up this week?
- Which invoices are still unpaid, oldest first?
- Summarize recent claims and their statuses.
- Show the most recent messages in my conversations that are about scheduling.

## Making changes (read and write key)

Anything that changes data needs a **read and write** key. Ask the assistant to show
you what it is about to change before it does, and review each change.

- Add a note to Margaret Alvarez's profile saying her daughter will call on Friday.
- Create an open shift for Thursday 9:00 to 13:00 for patient Robert Chen.
- Update caregiver Maria Gomez's availability to include Saturday mornings.

Assistants can misread a name or a date. Check the result in AveeCare, especially
before anything that touches a schedule or a patient's care.

## Tips

- Name the patient or caregiver in full, as it appears in AveeCare, when there could be two with the same first name.
- Ask the assistant to say which records it looked at, so you can check its work.
- Large questions use many requests, and each key may make 60 requests a minute. Narrow the window or the list if you hit the limit.
- Treat the answers as drafts: an assistant is not a clinician, and nothing it says replaces your agency's review.
