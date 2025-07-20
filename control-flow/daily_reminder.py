# daily_reminder.py

# Get user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Start processing the reminder
reminder = f"Reminder: {task} [Priority: {priority.capitalize()}]"

# Match-case for priority
match priority:
    case "high":
        reminder += " - This is a top-priority task."
    case "medium":
        reminder += " - You should complete this task soon."
    case "low":
        reminder += " - This can be done at your convenience."
    case _:
        reminder += " - (Unknown priority level)"

# Check if time-sensitive
if time_bound == "yes":
    reminder += " ⚠️ This task requires immediate attention today!"

# Output the final reminder
print("\n" + reminder)
