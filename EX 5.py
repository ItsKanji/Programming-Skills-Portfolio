def get_days_in_month(month, year):
    """Return the number of days in a given month, accounting for leap years."""
    # Dictionary mapping month numbers to days
    months = {
        1: ("January", 31),
        2: ("February", 28),  # Default for February
        3: ("March", 31),
        4: ("April", 30),
        5: ("May", 31),
        6: ("June", 30),
        7: ("July", 31),
        8: ("August", 31),
        9: ("September", 30),
        10: ("October", 31),
        11: ("November", 30),
        12: ("December", 31)
    }

    if month in months:
        month_name, days = months[month]
        # Check for leap year adjustment for February
        if month == 2:
            if is_leap_year(year):
                days += 1  # Add an extra day for leap years
        return month_name, days
    else:
        return None

def is_leap_year(year):
    """Check if a given year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def main():
    """Main function to run the program."""
    try:
        month = int(input("Enter the month number (1-12): "))
        year = int(input("Enter the year: "))

        result = get_days_in_month(month, year)
        
        if result:
            month_name, days = result
            print(f"{month_name} has {days} days.")
        else:
            print("Invalid month number. Please enter a number between 1 and 12.")
        
    except ValueError:
        print("Please enter valid integers for month and year.")

if __name__ == "__main__":
    main()
