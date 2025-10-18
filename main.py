import random

play_again = "y"

while play_again == "y":
    # Generate a random number
    c = random.randint(1, 100)

    # First guess
    s = int(input("Guess a number from 1 to 100: "))
    guesses = 1

    # Loop until correct
    while s != c:
        if s > c:
            s = int(input("Lower number please: "))
        elif s < c:
            s = int(input("Higher number please: "))

        guesses += 1

    # Final message
    print(f"\nYou took {guesses} guesses to find the right answer.")

    # Ask to play again
    play_again = input("\nDo you want to play again? (y/n): ").lower()
    
    while play_again not in ["y", "n"]:
        input("Please enter valid word (y/n): ")

print("Thanks for playing.")