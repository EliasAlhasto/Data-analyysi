import random

thrownDice = []

for _ in range(5):
    thrownDice.append(random.randint(1, 6))

    print("\nList of thrown dice numbers:")
    print(thrownDice)

    total_sum = sum(thrownDice)
    print("\nSum of the thrown dice numbers:", total_sum)

    highest_value = max(thrownDice)
print("\nHighest value is:", highest_value)