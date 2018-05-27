#Fortune Cookie Program
#Demonstrates the elif clause

import random

print("I sense your energy. Your fortune today is coming across my screen.")
print("You have...\n")

luck = random.randint(1,5)

if luck == 1:
    #notsolucky
    print("not so good luck")

elif luck == 2:
    #normal
    print("normal luck")   

elif luck == 3:
    #good luck
    print("good luck")

elif luck == 4:
    #super good luck
    print("super good luck")

elif luck == 5:
    #super bad luck
    print("super bad luck")


print("\ntoday...")

input("\n\nPress the enter key to exit.")
