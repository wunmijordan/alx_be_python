# daily_reminder.py

# Get user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Start processing the reminder
alert = f"Reminder: '{task}'"

# Match-case for priority
match priority:
    case "high":
        alert += " is a high priority task"
    case "medium":
        alert += " - You should complete this task soon."
    case "low":
        alert += " is a low-priority task. Consider completing it when you have free time."
    case _:
        alert += " - (Unknown priority level)"

# Check if time-sensitive
if time_bound == "yes":
    alert += " that requires immediate attention today!"

# Output the final reminder
print("\n" + alert)
