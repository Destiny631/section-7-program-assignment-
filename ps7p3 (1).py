# Initialize the counter for the number of students
student_count = 0

# Prompt the user to decide whether to continue
response = input("Do you want to continue? (Yes/No): ").strip()

# Start the while loop if the user answers "Yes"
while response.lower() == "yes":
    # Prompt the user for their last name and two exam scores
    last_name = input("Enter the student's last name: ").strip()
    exam1 = float(input("Enter the first exam score: "))
    exam2 = float(input("Enter the second exam score: "))

    # Calculate the average score
    average_score = (exam1 + exam2) / 2

    # Display the student's last name and average score
    print(f"Student: {last_name}")
    print(f"Average Score: {average_score:.2f}")

    # Increment the student count
    student_count += 1

    # Ask the user if they want to continue with another student
    response = input("Do you want to enter another student's data? (Yes/No): ").strip()

# After the loop ends, display the total number of students entered
print(f"\nTotal number of students entered: {student_count}")
