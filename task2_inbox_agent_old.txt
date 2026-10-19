from task1_knowledge_brain.main import ask_knowledge_brain


def draft_email_reply(email_text):
    brain_result = ask_knowledge_brain(email_text)

    return (
        "Hi,\n\n"
        "Thank you for contacting support.\n\n"
        f"{brain_result}\n\n"
        "Best regards,\nSupport Team"
    )
