
from enum import Enum
import sys


CARD_VALUES = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
}


FIVE_OF_A_KIND = 7
FOUR_OF_A_KIND = 6
FULL_HOUSE = 5
THREE_OF_A_KIND = 4
TWO_PAIRS = 3
PAIR = 2
HIGH_CARD = 1


def evaluate(cards):
    values = [CARD_VALUES[c] for c in cards]
    for card in values:
        if values.count(card) == 5:
            return FIVE_OF_A_KIND
        elif values.count(card) == 4:
            return FOUR_OF_A_KIND
        elif values.count(card) == 3:
            for others in [c for c in values if c != card]:
                if values.count(others) == 2:
                    return FULL_HOUSE
            return THREE_OF_A_KIND
        elif values.count(card) == 2:
            for others in [c for c in values if c != card]:
                if values.count(others) == 3:
                    return FULL_HOUSE
            for others in [c for c in values if c != card]:
                if values.count(others) == 2:
                    return TWO_PAIRS
            return PAIR
    return HIGH_CARD


class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.card_values = [CARD_VALUES[c] for c in cards]
        self.bid = bid
        self.evaluation = evaluate(cards)

    def __lt__(self, other):
        if self.evaluation != other.evaluation:
            return self.evaluation < other.evaluation
        for s, o in zip(self.card_values, other.card_values):
            if s != o:
                return s < o
        return False

    def __eq__(self, other):
        return self.evaluation == other.evaluation and self.cards == other.cards

    def __str__(self):
        eval = [0, 'HIGH_CARD', 'PAIR', 'TWO_PAIRS', 'THREE_OF_A_KIND', 'FULL_HOUSE', 'FOUR_OF_A_KIND', 'FIVE_OF_A_KIND'][self.evaluation]
        return f'Hand({self.cards}, {self.bid}, {eval})'


def parsed_hands(stream):
    for line in stream:
        cards, bid = line.strip().split()
        yield Hand(cards, int(bid))


def winnings(hands):
    result = []
    for rank, hand in enumerate(hands, 1):
        points = hand.bid * rank
        print(f"{rank} {hand.cards} {points}")
        result.append(hand.bid * rank)
    return result


print(sum(winnings(sorted(parsed_hands(sys.stdin)))))

