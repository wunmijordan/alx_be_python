monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses

print(f"Your monthly savings are ${int(monthly_savings)}.")

projected_savings = (monthly_savings * 12 + (monthly_savings * 12 * 0.05))

print(f"Projected savings after one year, with interest, is: ${int(projected_savings)}.")