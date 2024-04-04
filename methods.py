import heapq


class Auction:
    def __init__(self, min_bid):
        self.min_bid = min_bid
        self.bid_heap = []
        self.bidder_bids = {}
        self.unique_bids = {}
        self.current_highest_bid = None

    def place_bid(self, bidder_id, bid_amount):
        # Discard bids less than the minimum bid
        if bid_amount < self.min_bid:
            return "Bid amount must be higher than the minimum bid."

        # Record bid for the bidder
        if bidder_id in self.bidder_bids:
            self.bidder_bids[bidder_id].append(bid_amount)
        else:
            self.bidder_bids[bidder_id] = [bid_amount]

        # Insert bid into the priority queue
        heapq.heappush(self.bid_heap, (-bid_amount, bidder_id))

        # Update highest bid
        if not self.current_highest_bid or bid_amount > self.current_highest_bid[0]:
            self.current_highest_bid = (bid_amount, bidder_id)

        # Update unique bids
        if bid_amount in self.unique_bids:
            self.unique_bids[bid_amount] += 1
        else:
            self.unique_bids[bid_amount] = 1

    def find_winner(self):
        # If there are no bids, return None
        if not self.bid_heap:
            return None

        # Loop to handle tie-breaking logic
        while self.unique_bids.get(-self.current_highest_bid[0], 0) > 1:
            self.min_bid = self.current_highest_bid[0] + 1
            self.reset_auction()
            # Find the new highest bid after resetting the auction
            self.current_highest_bid = heapq.heappop(self.bid_heap)

        # Return the winner
        return self.current_highest_bid[1]

    def reset_auction(self):
        self.bid_heap = []
        self.unique_bids.clear()
        for bidder_id, bids in self.bidder_bids.items():
            for bid in bids:
                heapq.heappush(self.bid_heap, (-bid, bidder_id))
                if bid in self.unique_bids:
                    self.unique_bids[bid] += 1
                else:
                    self.unique_bids[bid] = 1

