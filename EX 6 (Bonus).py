# Define the correct password
correct_password = "12345"
max_attempts = 5
attempts = 0

# Use a while loop to repeatedly ask for the password
while attempts < max_attempts:
    user_input = input("Enter the password: ")
    
    # Check if the entered password is correct
    if user_input == correct_password:
        print("Access granted.")
        break  # Exit the loop if the password is correct
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print(f"Wrong password! You have {remaining_attempts} attempt(s) left.")
        else:
            print("Wrong password! The Authorities have been alerted.")
