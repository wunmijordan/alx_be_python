# daily_reminder.py

# Get user input
task = input("Enter the task: ")
priority = input("Enter the task’s priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

# Start processing the reminder
reminder = f"Reminder: '{task}'"

# Match-case for priority
match priority:
    case "high":
        reminder += " is a high priority task"
    case "medium":
        reminder += " - You should complete this task soon."
    case "low":
        reminder += " is a low-priority task. Consider completing it when you have free time."
    case _:
        reminder += " - (Unknown priority level)"

# Check if time-sensitive
if time_bound == "yes":
    reminder += " that requires immediate attention today!"

# Output the final reminder
print("\n" + reminder)
