import time
from enum import Enum

start_time = time.time()
import heapq as hp

class Card(Enum):
    T = 10
    J = 11
    Q = 12
    K = 13
    A = 14
    _9 = 9
    _8 = 8
    _7 = 7
    _6 = 6
    _5 = 5
    _4 = 4
    _3 = 3
    _2 = 2

# Create a dictionary to map card characters to their numeric values
card_values = {str(i): i for i in range(2, 10)}
card_values.update({k.name: k.value for k in Card})


class Hand:
    def __init__(self, cards, bid):
        self.bid = bid
        self.cards = [card_values[card] for card in cards]
        all_card = {}
        for card in cards:
            if all_card.get(card) is None:
                all_card[card] = 1
            else:
                all_card[card] += 1
        all_values = list(all_card.values())
        if max(all_values) == 5:
            self.total = 6
        elif max(all_values) == 4:
            self.total = 5
        elif 2 in all_values and 3 in all_values:
            self.total = 4
        elif max(all_values) == 3:
            self.total = 3
        elif len([i for i in all_values if i ==2]) == 2:
            self.total = 2
        elif max(all_values) == 2:
            self.total = 1
        else:
            self.total = 0

    def __lt__(self, other):
        if not isinstance(other, Hand):
            return NotImplemented
        if self.total != other.total:
            return self.total < other.total
        for a, b in zip(self.cards, other.cards):
            diff = a != b
            print(a, b, diff)
            if diff:
                print(a-b)
                return a < b

with open('input.txt', 'r') as f:
    hands, bids = zip(*[(part1, int(part2)) for line in f.readlines() for part1, part2 in [line.split()]])
    heap = []

    for hand, bid in zip(hands, bids):
        hp.heappush(heap, Hand(hand, bid))

    total = 0
    for i in range(1, len(hands) + 1):
        hand = hp.heappop(heap)
        total += i * hand.bid

    print(total)

    print(Card(card_values['A']).value)



    pass

end_time = time.time()
elapsed_time = end_time - start_time
print(f"The code took {elapsed_time} seconds to run.")