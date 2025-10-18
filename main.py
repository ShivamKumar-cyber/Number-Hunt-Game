import random  # To let the computer choose a random number

# 📝 Welcome message and clear instructions
print("\n🎯 Welcome to the Number Guessing Game!")
print("🤖 I (the computer) will secretly choose a number from 1 to 100.")
print("🧠 Your job is to guess the number.")
print("💡 After each guess, I’ll tell you if the number is bigger or smaller.")
print("Let's begin!\n")

play_again = "y"  # This controls whether the game repeats

while play_again == "y":
    # Computer secretly chooses a number
    secret_number = random.randint(1, 100)

    # Ask the player for their first guess
    guess = int(input("👉 Enter your guess (from 1 to 100): "))
    attempts = 1  # Track number of tries

    # Keep looping until the player guesses correctly
    while guess != secret_number:
        if guess > secret_number:
            guess = int(input("📉 The number is bigger. Try smaller: "))
        else:
            guess = int(input("📈 The number is smaller. Try bigger: "))
        attempts += 1

    # If the guess is correct 🎉
    print(f"\n✅ Correct! The number was {secret_number}.")
    print(f"🎉 You guessed it in {attempts} attempts.")

    # Ask if the player wants to play again
    play_again = input("\nDo you want to play again? (y/n): ").lower()
    while play_again not in ["y", "n"]:
        play_again = input("Please enter a valid choice (y/n): ").lower()

# Goodbye message
print("👋 Thanks for playing! See you next time!")
