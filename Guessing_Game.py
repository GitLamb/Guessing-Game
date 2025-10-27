#Jason Lambert
#CIS261
#Guessing Game
#10/26/b25

import random

# Part 1: Display heading
def display_heading():
    print("=" * 40)
    print(" Welcome to the Number Guessing Game ")
    print("=" * 40)

# Part 2: Play the game
def play_game(limit):
    secret_number = random.randint(1, limit)
    print(f"\nI'm thinking of a number between 1 and {limit}. Can you guess it?")
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if guess < secret_number:
                print("Too low. Try again.")
            elif guess > secret_number:
                print("Too high. Try again.")
            else:
                print("Congratulations! You guessed the correct number.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

# Main loop
def main():
    display_heading()
    while True:
        try:
            limit = int(input("\nEnter the upper limit for the guessing range: "))
            play_game(limit)
        except ValueError:
            print("Please enter a valid number for the limit.")
            continue
        again = input("\nWould you like to play again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thank you for playing. Goodbye!")
            break

# Run the program
if __name__ == "__main__":
    main()
