# Introduction
This document is an overview of the mock auction system that was designed as a part of the final project for the Data Structure course. This auction system sets up a simulation of 1000 bidders, each bidding between $10 - $1,000,000 in an auction system to showcase an example of a sorting algorithm. 
## System Overview

The auction system consists of the following components:
•	Auction Class: Responsible for managing the auction process, including bid submission, tie-breaking, and winner determination.
•	Priority Queue (Heap): Used to maintain bids in a priority order based on their amounts.
•	Data Structures: Dictionaries for storing bidder IDs, bid amounts, and unique bids.

## Architecture
### Component Diagram

Class: Auction
Attributes: 
•	min_bid
•	bid_heap   
•	bidder_bids 
•	unique_bids
•	current_highest_bid


### Interaction Flow
The flow of interacting with the application is as follows:
1.	The Auction begins.
2.	Bidders submit bids to the Auction.
3.	The currently running Auction updates its internal data structures.
4.	When finding the winner, the Auction handles tie-breaking logic.
5.	The winner is determined based on the highest unique bid.
6.	The Auction completes.

##  Data Structures

    bid_heap: Priority queue (heap) to store bids in a priority order based on their amounts.
    bidder_bids: HashMap (as Python Dictionary) to store bidder IDs and their bids.
    unique_bids: HashMap (as Python Dictionary) to store unique bids and their counts.
    current_highest_bid: Tuple to store the current highest bid amount and bidder ID.
Using Python’s Dictionary function as a HashMap allows HashMap’s to mitigate the chance of having a collision with each other automatically. Alongside this, using a tuple allows the list to remain immutable to quickly find the highest bid without searching through the list.







## Algorithms
### Placing a Bid

Input: Bidder ID, Bid Amount

•	Validate bid amount.
•	Insert bid into the priority queue (bid_heap).
•	Update bidder's bid history and unique bid counts.
•	Update the current highest bid if necessary.
    Complexity: O(log n) - Logarithmic time complexity for inserting into the priority queue.

### Finding the Winner

•	Loop through tied bids and handle tie-breaking logic.
•	Increment minimum bid and reset the auction if there is a tie.
•	Determine the winner based on the highest unique bid.
    Complexity: O(log n)

### Resetting the Auction

•	Clear auction data structures.
•	Rebuild the priority queue with remaining bids.
    Complexity: O(n log n) - Where ‘n’ is the number of bids.

## Implementation Details

This project was Implemented in Python, using the PyStorm IDE. To efficiently display the assignment, this project uses a ‘heapq’ module for the priority queue (Pythons heap) implementation. For ease of use and modulation, the program has been separated into two separate classes to keep the bidding and the main classes separate. 

## Conclusion

In conclusion, the Auction System effectively handles bid processing and winner determination using priority queues and tie-breaking logic. On a smaller scale, this program showcases how a program like this may be completed in Python and what the most efficient way to do it is.
