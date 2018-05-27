#coin flip

import random

heads = 0
tails = 0
count = 0

while count != 100:
    coin = random.randint(1,2)

    if coin == 1:
        heads += 1

    elif coin == 2:
        tails += 1

    count += 1

print("The number of heads is", heads)
print("The number of tails is", tails)

input("\nPress the enter key to exit.")
