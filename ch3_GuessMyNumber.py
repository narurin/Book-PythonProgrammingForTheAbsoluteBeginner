#Guess one number from 1 to 100

import random
print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

number = random.randint(1, 100)

guess = int(input("What's your guess? "))
tries = 1

while guess != number:
    if guess > number:
        print("Lower!\n")
    else:
        print("Higher!\n")

    guess = int(input("Try again! What's your guess? "))
    tries += 1

print("\nCongratulations! You have guessed the correct number.")
print("You took",tries,"guesses to get the answer!")


input("\n\nPress the enter key to exit.")
