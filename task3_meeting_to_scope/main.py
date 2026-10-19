# Task 3: Checks Task 1 to see if it's a built-in setting or custom code
from task1.main import ask_brain

def meeting_to_sow(client_request):
    ans = ask_brain(client_request)
    if "Found in Brilliant Directories" in ans:
        return f"Request: {client_request}\nType: Built-in Setting | 1 hr ($100)"
    return f"Request: {client_request}\nType: Custom Developer Code | 12 hrs ($1,200)"

def run():
    print("\n--- TASK 3: MEETING TO SCOPE OF WORK ---")
    print(meeting_to_sow("We need Google maps radius search"))
    print("----------------------------------------")
    print(meeting_to_sow("We need a custom mobile app for iOS"))

if __name__ == "__main__":
    run()
