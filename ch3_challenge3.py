#Guess one number from 1 to 100

import random
print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in 10 tries.\n")

number = random.randint(1, 100)
limit = 10

guess = int(input("What's your guess? "))
tries = 1


while tries != limit:
    if guess != number:
        if guess > number:
            print("Lower!\n")
        elif guess < number:
            print("Higher!\n")

        guess = int(input("Try again! What's your guess? "))
        tries += 1

    else:
        print("\nCongratulations! You have guessed the correct number.")
        print("You took",tries,"guesses to get the answer!")
        input("\n\nPress the enter key to exit.")
        break


print("\nToo bad! You couldn't get the answer within 10 tries!")
input("\n\nPress the enter key to exit.")


