import random

names = input("Give me everybody's name separated by a comma: ").split(",")
# print(names)

print(f"{random.choice(names)} will pay for the bills this month, lol!")