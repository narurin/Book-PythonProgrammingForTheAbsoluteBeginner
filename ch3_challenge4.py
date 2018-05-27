#Provide one number from 1 to 100
#for computer to guess

import random
print("\tWelcome to 'Guess My Number'!")
print("\nInput a number between 1 and 100.")
print("Lets see if the computer can guess it in 10 tries.\n")


number = int(input("What's your number? "))

if number > 100 or number < 1:
    print("Please enter a number between 1 and 100.")
    number = int(input("What's your number? "))

guess = random.randint(1, 100)
limit = 10
tries = 1


while tries <= limit:
    if guess != number:
        if guess > number:
            print("Lower!\n")
            guess = random.randint((guess-20), guess)
        elif guess < number:
            print("Higher!\n")
            guess = random.randint(guess, (guess+20))
            
        tries += 1

    else:
        print("The computer took",tries,"guesses to get the answer!")
        input("\n\nPress the enter key to exit.")
        break

    print(guess)


print("\nToo bad! The computer couldn't get the answer within 10 tries!")
input("\n\nPress the enter key to exit.")


