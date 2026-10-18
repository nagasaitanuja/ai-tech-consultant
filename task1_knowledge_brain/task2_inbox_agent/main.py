def draft_email_reply(email_text):
    """Drafts an email reply citing the Brilliant Directories article."""
    brain_result = ask_knowledge_brain(email_text)
    return (
        f"Hi,\n\n"
        f"Thank you for contacting support.\n\n"
        f"{brain_result}\n\n"
        f"Best regards,\nSupport Team"
    )
