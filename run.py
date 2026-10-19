
from task1_knowledge_brain.main import (
    load_brilliant_directories_sitemap,
    ask_knowledge_brain,
)
from task2_inbox_agent.main import draft_email_reply
from task3_meeting_to_scope.main import create_sow


def process_input(user_input):
    text = user_input.lower()

    if "we need" in text or "want to add" in text:
        return create_sow(user_input)

    if (
        text.startswith("dear ")
        or text.startswith("hello")
        or text.startswith("hi ")
    ):
        return draft_email_reply(user_input)

    return ask_knowledge_brain(user_input)


def main():
    print("AI Tech Consultant")
    print("Ask a question, draft an email, or describe a requirement.")
    print("Type 'exit' to quit.")

    load_brilliant_directories_sitemap()

    while True:
        try:
            user_input = input("\nEnter your request: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break

        if user_input.lower() == "exit":
            break

        if user_input:
            try:
                print(process_input(user_input))
            except Exception as error:
                print(f"Error processing request: {error}")


if __name__ == "__main__":
    main()

