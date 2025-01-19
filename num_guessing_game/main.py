import random

# Define range
lower_bound = 1
upper_bound = 100

# Generate the secret number
secret_number = random.randint(lower_bound, upper_bound)


# Define difficulty levels
def get_level():
    while True:
        try:
            diff_level = int(input("Enter your choice: "))
            if diff_level == 1:
                print("\nGreat! You have selected the Easy level.\nLet's start the game!\n")
                return 10  # max_attempts for Easy
            elif diff_level == 2:
                print("\nGreat! You have selected the Medium level.\nLet's start the game!\n")
                return 5  # max_attempts for Medium
            elif diff_level == 3:
                print("\nGreat! You have selected the Hard level.\nLet's start the game!\n")
                return 3  # max_attempts for Hard
            else:
                print("Invalid input. Please enter a valid number (1, 2, or 3).")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Get the user's guess
def get_guess():
    while True:
        try:
            guess = int(input(f"Enter your guess: "))
            if lower_bound <= guess <= upper_bound:
                return guess
            else:
                print(f"Invalid input. Please enter a number between {lower_bound} and {upper_bound}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Play the game
def play_game():
    max_attempts = get_level()  # Get the difficulty level and set max_attempts
    attempts = 0
    won = False

    while attempts < max_attempts:
        attempts += 1
        print(f"Attempt {attempts} of {max_attempts}")
        guess = get_guess()

        if guess == secret_number:
            print(f"🎉 Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
            won = True
            break
        elif guess < secret_number:
            print("Too low! Try again.\n")
        else:
            print("Too high! Try again.\n")

    if not won:
        print(f"😞 Sorry, you ran out of attempts! The secret number was {secret_number}.")


# Main program
if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")
    print("\nPlease select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)")
    print(" ")
    play_game()
