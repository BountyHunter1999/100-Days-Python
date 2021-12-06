import os
import time
from logo import logo

print(logo)

# print("lol")
# time.sleep(2.4)
os_name  = os.name
os_clear = 'cls' if os_name == 'nt' else 'clear'


# print("LOL AGAIN")
bidders = []

def add_bidder(name, cash):
    bidders.append({
        "name": name,
        "cash": cash
    })

def top_bidder(bidders):
    highest_bid = 0
    auction_winner = ""
    for bidder in bidders: # gives dictionary here
        if bidder["cash"] > highest_bid:
            auction_winner = bidder["name"]
            highest_bid = bidder["cash"]
    
    print(f"The winner of the auction is {auction_winner} with ${highest_bid}")

while True:
    name = input("Enter your name: ")
    cash = int(input("Enter the amount you want to bid: $"))
    add_bidder(name, cash)

    other = input("Are there any other players? Y or N? ").lower()
    if other == "y":
        os.system(os_clear)
    else:
        top_bidder(bidders)
        break