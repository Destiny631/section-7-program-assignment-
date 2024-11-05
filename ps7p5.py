# Initialize variable to keep track of the total discount
total_discount = 0

# Prompt the user to decide whether to continue with the program
response = input("Do you want to enter order data? (Yes/No): ").strip()

# Start the while loop if the user answers "Yes"
while response.lower() == "yes":
    # Prompt the user for the quantity and price of an item
    quantity = int(input("Enter the quantity of the item: "))
    price = float(input("Enter the price of the item: "))

    # Compute the extended price (quantity * price)
    extended_price = quantity * price

    # Determine the discount based on the extended price
    if extended_price > 10000:
        discount_percent = 0.25  # 25% discount
    else:
        discount_percent = 0.10  # 10% discount

    # Calculate the discount amount
    discount_amount = extended_price * discount_percent

    # Calculate the total after the discount
    total_price = extended_price - discount_amount

    # Display the order details
    print(f"Extended Price: ${extended_price:.2f}")
    print(f"Discount Amount: ${discount_amount:.2f}")
    print(f"Total Price after Discount: ${total_price:.2f}")

    # Add the discount amount to the total discount
    total_discount += discount_amount

    # Ask the user if they want to enter another order
    response = input("Do you want to enter another order? (Yes/No): ").strip()

# After the loop ends, display the total discount
print(f"\nTotal discount given: ${total_discount:.2f}")
# Initialize variable to keep track of the total discount
total_discount = 0

# Prompt the user to decide whether to continue with the program
response = input("Do you want to enter order data? (Yes/No): ").strip()

# Start the while loop if the user answers "Yes"
while response.lower() == "yes":
    # Prompt the user for the quantity and price of an item
    quantity = int(input("Enter the quantity of the item: "))
    price = float(input("Enter the price of the item: "))

    # Compute the extended price (quantity * price)
    extended_price = quantity * price

    # Determine the discount based on the extended price
    if extended_price > 10000:
        discount_percent = 0.25  # 25% discount
    else:
        discount_percent = 0.10  # 10% discount

    # Calculate the discount amount
    discount_amount = extended_price * discount_percent

    # Calculate the total after the discount
    total_price = extended_price - discount_amount

    # Display the order details
    print(f"Extended Price: ${extended_price:.2f}")
    print(f"Discount Amount: ${discount_amount:.2f}")
    print(f"Total Price after Discount: ${total_price:.2f}")

    # Add the discount amount to the total discount
    total_discount += discount_amount

    # Ask the user if they want to enter another order
    response = input("Do you want to enter another order? (Yes/No): ").strip()

# After the loop ends, display the total discount
print(f"\nTotal discount given: ${total_discount:.2f}")
