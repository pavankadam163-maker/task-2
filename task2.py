import random

def guess_the_number():
    print("🎯 Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.\n")

    while True:
        number = random.randint(1, 100)
        attempts = 0

        while True:
            try:
                guess = int(input("👉 Enter your guess: "))
                attempts += 1
            except ValueError:
                print("⚠️ Please enter a valid number.")
                continue

            if guess < number:
                print("⬇️ Too low! Try again.\n")
            elif guess > number:
                print("⬆️ Too high! Try again.\n")
            else:
                print(f"🎉 Correct! The number was {number}.")
                print(f"🏆 You guessed it in {attempts} attempts!\n")
                break

        play_again = input("Would you like to play again? (yes/no): ").strip().lower()
        if play_again not in ("yes", "y"):
            print("👋 Thanks for playing! Goodbye!")
            break

# Run the game
guess_the_number()
