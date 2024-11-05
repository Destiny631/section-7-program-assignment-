# Get user input for start, stop, and increment values
start = int(input("Enter the start value: "))
stop = int(input("Enter the stop value: "))
increment = int(input("Enter the increment value: "))

# Initialize the current value to the start value
current = start

# Use a while loop to display the numbers
while current <= stop:
    print(current)  # Display the current number
    current += increment  # Increment the current value by the specified increment
