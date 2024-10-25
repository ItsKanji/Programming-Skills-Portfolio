# Define a function for the quiz
def quiz():
    # Dictionary of countries and their capitals
    capitals = {
        "France": "Paris",
        "Germany": "Berlin",
        "Italy": "Rome",
        "Spain": "Madrid",
        "Portugal": "Lisbon",
        "Netherlands": "Amsterdam",
        "Belgium": "Brussels",
        "Sweden": "Stockholm",
        "Norway": "Oslo",
        "Finland": "Helsinki"
    }
    
    # Loop through the dictionary and ask questions
    for country, capital in capitals.items():
        answer = input(f"What is the capital of {country}? ").strip()
        
        #Check the answer ignoring capitalization
        if answer.lower() == capital.lower():
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is {capital}.")

# Run the quiz
quiz()
