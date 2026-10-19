
from task1_knowledge_brain.main import ask_brain


def reply_email(email_text):
    message = email_text.strip()
    answer = ask_brain(message)

    if "I don't know" in answer or "Escalated" in answer:
        reply = (
            "Thank you for your message.\n\n"
            "We need to review your request to provide an "
            "accurate response. Our support team will "
            "follow up after checking the details."
        )
    elif "quote" in message.lower():
        reply = (
            "Thank you for confirming that the quote "
            "has been approved.\n\n"
            "We have noted your update. Please let us know "
            "if you have any questions or need further "
            "assistance with the next steps."
        )
    else:
        reply = (
            "Thank you for contacting support.\n\n"
            "Based on our current knowledge base, here is "
            "the relevant information:\n\n"
            f"{answer}\n\n"
            "Please let us know if you need further help."
        )

    return (
        "Subject: Re: Your Support Request\n\n"
        "Hi,\n\n"
        f"{reply}\n\n"
        "Best regards,\n"
        "Support Team"
    )


