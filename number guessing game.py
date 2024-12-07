import random

# Function for the number guessing game
def number_guessing_game():
    # Display a welcome message
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    # Number of attempts the player has
    attempts = 0

    while True:
        try:
            # Ask the player to guess the number
            guess = int(input("Make a guess: "))
            attempts += 1

            # Check if the guess is correct, too high or too low
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} correctly in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")

# Run the game
number_guessing_game()

