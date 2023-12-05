import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Set the maximum number of attempts
    max_attempts = 3
    attempts_left = max_attempts
    
    while attempts_left > 0:
        # Ask the user to guess the number
        user_guess = int(input("Guess the number between 1 and 100: "))
        
        # Check if the guess is correct
        if user_guess == secret_number:
            print(f"Congratulations! You guessed the correct number in {max_attempts - attempts_left + 1} attempts.")
            break
        elif user_guess < secret_number:
            print(f"Too low! Try again. Attempts left: {attempts_left - 1}.")
        else:
            print(f"Too high! Try again. Attempts left: {attempts_left - 1}.")
        
        # Decrease the number of attempts left
        attempts_left -= 1
    
    # If the user couldn't guess the number
    if attempts_left == 0:
        print(f"Sorry, you're out of attempts. The correct number was {secret_number}.")
    
    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        guess_the_number()

# Test the program with correct guesses
guess_the_number()

# Test the program with incorrect guesses
guess_the_number()

# Verify that the game restarts after completion
guess_the_number()
