import random

thrownDice = []

for _ in range(5):
    thrownDice.append(random.randint(1, 6))

    print("\nList of thrown dice numbers:")
    print(thrownDice)