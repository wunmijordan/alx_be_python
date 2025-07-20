# multiplication_table.py

try:
    number = int(input("Enter a number to see its multiplication table: "))

    print(f"\nMultiplication Table for {number}:\n")
    for i in range(1, 11):
        result = number * i
        print(f"{number} * {i} = {result}")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
