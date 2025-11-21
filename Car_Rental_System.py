print("========================================")
print("     Welcome to G4 Car Rental Shop")
print("========================================")

#loop if the user input is invalid
while True:
    print("Available Vehicles:")
    print("1 - Toyota Vios (₱1500/day or ₱200/hour)")
    print("2 - Mitsubishi Xpander (₱2500/day or ₱300/hour)")
    print("3 - Toyota Hilux (₱2100/day or ₱280/hour)")

    vehicle_choice = input("Choose a vehicle (1-3): ")

    if vehicle_choice in ["1", "2", "3"]:
        vehicle_choice = int(vehicle_choice)
        break
    else:
        print("Invalid choice! Please choose a number between 1 and 3.\n")

# Rent type selection
while True:
    print("Rent type:")
    print("1 - Per Day")
    print("2 - Per Hour")
    rent_type = input("Choose rent type (1-2): ")

    if rent_type in ["1", "2"]:
        rent_type = int(rent_type)
        break
    else:
        print("Invalid rent type! Please choose 1 or 2.\n")

# Select vehicle name and rate
if vehicle_choice == 1:
    vehicle_type = "Toyota Vios"
    day_rate = 1500
    hour_rate = 200
elif vehicle_choice == 2:
    vehicle_type = "Mitsubishi Xpander"
    day_rate = 2500
    hour_rate = 300
elif vehicle_choice == 3:
    vehicle_type = "Toyota Hilux"
    day_rate = 2100
    hour_rate = 280

# Quantity of vehicles
while True:
    try:
        quantity = int(input("How many vehicles would you like to rent? "))
        if quantity > 0:
            break
        else:
            print("Quantity must be at least 1.")
    except ValueError:
        print("Invalid input! Enter a number.\n")

# Rent duration
if rent_type == 1:
    while True:
        try:
            duration = int(input("Enter number of days to rent: "))
            if duration > 0:
                break
            else:
                print("Duration must be at least 1.")
        except ValueError:
            print("Please enter a valid number.\n")

    total_payment = day_rate * duration * quantity
    rent_basis = "day(s)"

elif rent_type == 2:
    while True:
        try:
            duration = int(input("Enter number of hours to rent: "))
            if duration > 0:
                break
            else:
                print("Duration must be at least 1.")
        except ValueError:
            print("Please enter a valid number.\n")

    total_payment = hour_rate * duration * quantity
    rent_basis = "hour(s)"

# Customer Info
print("--- Customer Information ---")
name = input("Enter your full name: ")
contact = input("Enter your contact number: ")
valid_id = input("Enter your valid ID type: ")

# Summary
print("--- Rental Summary ---")
print(f"Customer Name: {name}")
print(f"Contact Number: {contact}")
print(f"Valid ID: {valid_id}")
print(f"Vehicle Rented: {vehicle_type}")
print(f"Quantity: {quantity}")
print(f"Rental Duration: {duration} {rent_basis}")
print(f"Total Payment: ₱{total_payment:.2f}")

# Payment section
while True:
    try:
        payment = float(input("Enter payment amount: ₱"))
        if payment >= total_payment:
            change = payment - total_payment
            print("Payment successful!")
            print(f"Change: ₱{change:.2f}")
            break
        else:
            print("Insufficient payment! Please pay the full amount.")
    except ValueError:
        print("Invalid amount! Please enter a valid number.\n")

# Simulate record update
print("Updating records...")
print("Vehicle status: RENTED")
print("Customer info recorded successfully.")
print("--- Receipt Generated ---")
print(f"Thank you, {name}, for renting {quantity} unit(s) of {vehicle_type}!")
print("Please return the vehicle on time and in good condition.")
print("===================================")
print("       End of Transaction          ")
print("===================================")
