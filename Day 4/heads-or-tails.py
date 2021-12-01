import random

coin = {
    "h": 1,
    "t": 0
}
a = input("Choose heads or tails: h or t =>").lower()

random_side = random.randint(0,1)

if random_side == coin[a]:
    print("You Got what u wished for")
else:
    print("Sad! You got the exact opposite")

print(f"random number was: {random_side}")