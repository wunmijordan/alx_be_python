# daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

print("\n--- DAILY TASK REMINDER ---\n")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"🔥 URGENT: '{task}' is a HIGH priority task that requires immediate attention today!")
        else:
            print(f"⚠️ Reminder: '{task}' is a HIGH priority task. Please make it a top priority soon.")
    case "medium":
        if time_bound == "yes":
            print(f"⏰ Reminder: '{task}' is a MEDIUM priority task and should be completed today.")
        else:
            print(f"📅 Reminder: '{task}' is a MEDIUM priority task. Schedule time for it this week.")
    case "low":
        if time_bound == "yes":
            print(f"🔔 Heads Up: '{task}' is a LOW priority task, but it has a deadline today.")
        else:
            print(f"📝 Note: '{task}' is a LOW priority task. Handle it when you have free time.")
    case _:
        print("⚠️ Invalid priority level entered. Please use: high, medium, or low.")

print("\n💪 Have a focused day!")
