from methods import Auction

import random
from methods import Auction

auction = Auction(min_bid=10)

for i in range(1, 1001):
    bidder_id = f"Bidder{i}"
    bid_amount = random.randint(1, 1000000)  # Generate random bid amount
    auction.place_bid(bidder_id, bid_amount)

# Find the winner
winner = auction.find_winner()
winning_bid_amount = auction.current_highest_bid[0]

if winner:
    print("Winner:", winner)
    print("With the bid of: ", winning_bid_amount)
else:
    print("No winner. No bids were submitted or all bids were below the minimum bid.")
