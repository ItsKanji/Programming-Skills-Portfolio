def check_even_odd(number):
    """Determine if the number is even or odd."""
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

def main():
    """Main function to run the program."""
    try:
        # Ask the user for a number
        user_input = int(input("Please enter a number: "))
        
        # Call the function to check if the number is even or odd
        result = check_even_odd(user_input)
        
        # Print the result
        print(result)
        
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
