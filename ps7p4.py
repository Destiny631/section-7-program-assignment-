# Initialize variables for the total gross pay and employee count
total_gross_pay = 0
employee_count = 0

# Prompt the user to decide whether to continue
response = input("Do you want to enter employee data? (Yes/No): ").strip()

# Start the while loop if the user answers "Yes"
while response.lower() == "yes":
    # Prompt the user for employee details
    last_name = input("Enter the employee's last name: ").strip()
    hours_worked = float(input("Enter the number of hours worked: "))
    rate_of_pay = float(input("Enter the employee's hourly rate of pay: "))

    # Compute gross pay, considering time and a half for overtime (over 40 hours)
    if hours_worked > 40:
        regular_hours = 40
        overtime_hours = hours_worked - 40
        overtime_rate = rate_of_pay * 1.5  # Time and a half
        gross_pay = (regular_hours * rate_of_pay) + (overtime_hours * overtime_rate)
    else:
        gross_pay = hours_worked * rate_of_pay

    # Display the employee's last name and gross pay
    print(f"Employee: {last_name}, Gross Pay: ${gross_pay:.2f}")

    # Add gross pay to the total and increment the employee count
    total_gross_pay += gross_pay
    employee_count += 1

    # Ask the user if they want to continue entering more employees
    response = input("Do you want to enter another employee's data? (Yes/No): ").strip()

# After the loop ends, display the total gross pay and employee count
print(f"\nTotal number of employees entered: {employee_count}")
print(f"Total gross pay for all employees: ${total_gross_pay:.2f}")

# Compute and display the average gross pay
if employee_count > 0:
    average_pay = total_gross_pay / employee_count
    print(f"Average gross pay: ${average_pay:.2f}")
else:
    print("No employee data was entered.")
