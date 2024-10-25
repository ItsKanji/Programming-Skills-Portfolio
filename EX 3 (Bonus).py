# Create a dictionary to store user information
user_info = {}

# Get user input for name, hometown, and age
name = input("Enter your name (first and last): ")
hometown = input("Enter your hometown: ")

# Input validation for age
while True:
    age = input("Enter your age: ")
    # Check if the input is a valid number
    if age.isdigit():  # This checks if the input is numeric
        user_info['age'] = int(age)  # Convert to integer and store
        break  # Exit the loop if input is valid
    else:
        print("Please enter a valid age as a number.")

# Store the information in the dictionary
user_info['name'] = name
user_info['hometown'] = hometown

# Print the values on separate lines
print("Your Information:")
print("Name:", user_info['name'])
print("Hometown:", user_info['hometown'])
print("Age:", user_info['age'])
