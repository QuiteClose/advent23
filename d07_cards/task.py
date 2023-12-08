from collections import namedtuple
from functools import cmp_to_key
from operator import itemgetter
import sys

# ~~~~~~~~
TASK = 2
# ~~~~~~~~


Trick = namedtuple('Trick', ['hand', 'bid'])
CARDS = '23456789TJQKA' if TASK == 1 else 'J23456789TQKA'
HANDS = [
    ('five_of_a_kind',  7, lambda a: set_of(5, a)),
    ('four_of_a_kind',  6, lambda a: set_of(4, a)),
    ('full_house',      5, lambda a: set_of(3, a) and set_of(2, a)),
    ('three_of_a_kind', 4, lambda a: set_of(3, a)),
    ('two_pair',        3, lambda a: len(pairs(a)) == 2),
    ('one_pair',        2, lambda a: set_of(2, a)),
    ('high_card',       1, lambda a: True),
]


def card_count(hand):
    return {card: hand.count(card) for card in hand}


def pairs(hand):
    return [card for card, count in card_count(hand).items() if count == 2]


def set_of(n, hand):
    return any(count == n for count in card_count(hand).values())


def substitute_joker(hand):
    most_to_least = reversed(sorted(card_count(hand).items(), key=itemgetter(1)))
    for substitute, _ in most_to_least:
        if substitute != 'J':
            return [
                substitute if card == 'J' else card for card in hand
            ]
    return hand


def evaluate(hand):
    if 'J' in hand and TASK == 2:
        hand = substitute_joker(hand)
    for name, value, condition in HANDS:
        if condition(hand):
            return value


def compare_cards(a, b):
    a_value = list(map(CARDS.index, a.hand))
    b_value = list(map(CARDS.index, b.hand))
    if a_value > b_value:
        return 1
    elif a_value < b_value:
        return -1
    return 0


def compare(a, b):
    a_value = evaluate(a.hand)
    b_value = evaluate(b.hand)
    if a_value > b_value:
        return 1
    elif a_value < b_value:
        return -1
    return compare_cards(a, b)


def winnings(records):
    for rank, trick in records:
        print(f'{rank} {trick.hand} {rank*trick.bid}')
        yield rank*trick.bid


def parse(stream):
    for line in stream:
        hand, bid = line.strip().split()
        yield Trick(hand, int(bid))


print(sum(winnings(enumerate(sorted(parse(sys.stdin), key=cmp_to_key(compare)), start=1))))

