from task1.main import ask_brain

streak = 0
autopilot = False

def reply_email(email_text):
    global streak, autopilot
    answer = ask_brain(email_text)
    streak += 1
    if streak >= 20:
        autopilot = True
    return f"Hi,\n\n{answer}\n\nBest regards,\nSupport Team"

def run():
    print("\n--- TASK 2: INBOX AGENT ---")
    print(reply_email("How to setup Stripe payment gateway?"))
    print("Autopilot active (after 20 emails)?:", streak >= 20)

if __name__ == "__main__":
    run()
