#Provide one number from 1 to 100
#for computer to guess

import random

upper_limit = 100
lower_limit = 1
attempt_limit = 5

print("\tWelcome to 'Guess My Number'!")
print("\nInput a number between",lower_limit,"and",upper_limit,".")
print("Lets see if the computer can guess it in",attempt_limit,"tries.\n")


number = int(input("What's your number? "))

if number > upper_limit or number < lower_limit:
    print("Please enter a number between",lower_limit,"and",upper_limit,".")
    number = int(input("What's your number? "))

guess = (upper_limit + lower_limit) // 2
tries = 1

while tries <= attempt_limit:
    print("guess:", guess)
    if guess == number:
        print("The computer took",tries,"guesses to get the answer!")
        input("\n\nPress the enter key to exit.")
        break

    else:
        if guess > number:
            print("Lower!\n")
            upper_limit = guess - 1
        elif guess < number:
            print("Higher!\n")
            lower_limit = guess + 1
        guess = (upper_limit + lower_limit) // 2           
        tries += 1

if tries > attempt_limit:
    print("\nToo bad! The computer couldn't get the answer within",attempt_limit,"tries!")
    input("\n\nPress the enter key to exit.")


