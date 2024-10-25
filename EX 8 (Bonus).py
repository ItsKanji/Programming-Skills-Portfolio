# Initialize the list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Function to search for a name in the list
def search_name(name_to_search):
    if name_to_search in names:
        return f"{name_to_search} is in the list."
    else:
        return f"{name_to_search} is not in the list."

# Main program
# Allows the user to input the search term
user_input = input("Enter a name to search for: ")

# Search for the name and print the result
result = search_name(user_input)
print(result)
