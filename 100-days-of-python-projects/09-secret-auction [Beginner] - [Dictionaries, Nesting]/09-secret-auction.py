import os
from art import logo

print(logo)
print("Welcome to the secret auction program.")
auction={}

def highest_bid(bids):
    highest = 0
    winner=""
    for bid in bids:
        bid_amount = bids[bid]
        if bid_amount>highest:
            highest=bid_amount
            winner = bid
    print(f"The winner is {winner} with the bid ${highest}")


loop = True
while loop:
    name = input("What is your name? :",)
    bid = int(input("What is your bid? $",))
    auction[name]=bid
    print(auction.keys(),auction.values())
    should_continue =input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if should_continue=='yes':
        os.system('cls')
    elif should_continue=='no':
        highest_bid(auction)
        loop=False








    

