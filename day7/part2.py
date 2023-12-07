import time
from enum import Enum
import heapq as hp

start_time = time.time()

mapping = {'A': 14, 'K': 13, 'Q': 12, 'J': 0, 'T': 10}


def card_to_int(char):
    if char.isdigit():
        return int(char)
    return mapping[char]


class Hand:
    def __init__(self, cards, bid):
        self.bid = bid
        self.cards = [card_to_int(card) for card in cards]
        all_card = {}
        for card in self.cards:
            if all_card.get(card) is None:
                all_card[card] = 1
            else:
                all_card[card] += 1
        nb_j = 0
        if all_card.get(0) is None:
            all_values = list(all_card.values())
        else:
            nb_j = all_card[0]
            all_card[0] = 0
            all_values = sorted(all_card.values(), reverse=True)
            all_values[0] += nb_j

        if max(all_values) == 5:
            self.total = 6
        elif max(all_values) == 4:
            self.total = 5
        elif 2 in all_values and 3 in all_values:
            self.total = 4
        elif max(all_values) == 3:
            self.total = 3
        elif len([i for i in all_values if i == 2]) == 2:
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
            if diff:
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

end_time = time.time()
elapsed_time = end_time - start_time
print(f"The code took {elapsed_time} seconds to run.")
