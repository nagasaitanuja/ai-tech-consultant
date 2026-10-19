
from task1_knowledge_brain.main import ask_brain


def reply_email(email_text):
    answer = ask_brain(email_text)

    if "I don't know" in answer or "Escalated" in answer:
        body = (
            "Thank you for contacting support.\n\n"
            "We could not find a confirmed answer in our "
            "current knowledge base. Our support team will "
            "need to review your request."
        )
    else:
        body = (
            "Thank you for contacting support.\n\n"
            "Regarding your request, please refer to the "
            "following documentation for guidance:\n\n"
            f"{answer}\n\n"
            "Please let us know if you need any further help."
        )

    return (
        "Subject: Re: Your Support Request\n\n"
        "Hi,\n\n"
        f"{body}\n\n"
        "Best regards,\n"
        "Support Team"
    )


def run():
    email = input("Enter the customer's email/message: ")
    print("\n--- GENERATED EMAIL DRAFT ---\n")
    print(reply_email(email))


if __name__ == "__main__":
    run()

