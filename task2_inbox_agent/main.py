consecutive_approvals = 0
autopilot_active = False
def draft_email_reply(email_text):
    """Drafts an email reply using Task 1 Knowledge Brain."""
    brain_result = ask_knowledge_brain(email_text)
    return (
        f"Hi,\n\n"
        f"Thank you for contacting support.\n\n"
        f"{brain_result}\n\n"
        f"Best regards,\nSupport Team"
    )
def review_draft(was_edited):
    """20 unedited approvals in a row unlocks Autopilot."""
    global consecutive_approvals, autopilot_active
    if not was_edited:
        consecutive_approvals += 1
        if consecutive_approvals >= 20:
            autopilot_active = True
    else:
        consecutive_approvals = 0
