
from task1_knowledge_brain.main import ask_brain
from task2_inbox_agent.main import reply_email
from task3_meeting_to_scope.main import meeting_to_sow

def main():
    print("=== AI TECH CONSULTANT ===")
    print("1. Ask a knowledge-base question")
    print("2. Draft an email reply")
    print("3. Estimate a meeting requirement")
    print("Type exit to quit.")

    while True:
        choice = input("\nChoose task (1/2/3): ").strip()

        if choice.lower() == "exit":
            print("Goodbye!")
            break

        if choice == "1":
            question = input("Enter your question: ")
            print(ask_brain(question))

        elif choice == "2":
            email = input("Enter the customer's email/message: ")
            print(reply_email(email))

        elif choice == "3":
            requirement = input("Enter the client requirement: ")
            print(meeting_to_sow(requirement))

        else:
            print("Please enter 1, 2, 3, or exit.")


if __name__ == "__main__":
    main()
