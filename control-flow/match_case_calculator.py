# match_case_calculator.py

# Prompt for user input
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose the operation (+, -, *, /): ")

    # Perform calculation using match-case
    match operation:
        case "+":
            result = num1 + num2
            print(f"The result is {result}:0f")
        case "-":
            result = num1 - num2
            print(f"The result is {result:.0f}.")
        case "*":
            result = num1 * num2
            print(f"The result is {result:.0f}.")
        case "/":
            if num2 != 0:
                result = num1 / num2
                print(f"The result is {result:.0f}.")
            else:
                print("Error: Cannot divide by zero.")
        case _:
            print("Invalid operation selected.")

except ValueError:
    print("Invalid input. Please enter valid numbers.")
