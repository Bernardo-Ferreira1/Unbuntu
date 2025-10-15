# 1. INITIAL GUEST FILE CREATION
# --------------------------------------------
# Open "guests.txt" in write mode ("w")
# If file exists, it will be overwritten
guests = open("guests.txt", "w")

# Initial list of guests who checked in
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

# Write each guest to file, one per line
for i in initial_guests:
    guests.write(i + "\n")  # "\n" creates new line after each name
    
# Close file to release resources
guests.close()

# Verification: Read and print all current guests
with open("guests.txt") as guests:
    for line in guests:
        print(line.strip())  # .strip() removes extra spaces and newlines


# 2. ADD NEW GUESTS (CHECK-IN)
# ---------------------------------------
# New guests who arrived at the hotel
new_guests = ["Sam", "Danielle", "Jacob"]

# Open file in append mode ("a") to add to the end
# "with" ensures file is automatically closed
with open("guests.txt", "a") as guests:
    for i in new_guests:
        guests.write(i + "\n")

# Verification: Show updated guest list
with open("guests.txt") as guests:
    for line in guests:
        print(line.strip())


# 3. PROCESS CHECK-OUTS (REMOVE GUESTS)
# -------------------------------------------
# Guests who checked out and should be removed
checked_out = ["Andrea", "Manuel", "Khalid"]
temp_list = []  # Temporary list to store active guests

# Read all current guests and store in temporary list
with open("guests.txt", "r") as guests:
    for g in guests:
        temp_list.append(g.strip())  # .strip() removes \n and spaces

# Rewrite complete file, excluding those who checked out
with open("guests.txt", "w") as guests:
    for name in temp_list:
        if name not in checked_out:
            guests.write(name + "\n")  # Keep only those who didn't leave

# Verification: Show list after check-outs
with open("guests.txt") as guests:
    for line in guests:
        print(line.strip())


# 4. CHECK STATUS OF SPECIFIC GUESTS
# --------------------------------------------
# List of guests to verify if they are present
guests_to_check = ['Bob', 'Andrea']
checked_in = []  # List to store current guests

# Read all current guests into checked_in list
with open("guests.txt", "r") as guests:
    for g in guests:
        checked_in.append(g.strip())

# Check status of each guest in the verification list
for check in guests_to_check:
    if check in checked_in:
        print("{} is checked in".format(check))  # Still at hotel
    else:
        print("{} is not checked in".format(check))  # Already checked out

