import auction_logo
import os

print(auction_logo.logo)

print("Welcome to the secret auction program.")

def maximum_bid(bids):
    winner = ""
    max_bid = 0
    for bidder in bids:
        if max_bid < bids[bidder]:
            winner = bidder
            max_bid = bids[bidder]
    print(f"The winner is {winner} with a bid of ${max_bid}")

auction = {}

while True:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    auction[name] = bid
    another_bid = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if another_bid != "yes":
        maximum_bid(auction)
        break
    os.system('cls')