
from collections import namedtuple
import sys


Card = namedtuple('Card', 'index numbers winning')


def parse(line):
    details, game = line.strip().split(':')
    numbers, winning = game.strip().split('|')
    return Card(
        index=int(details.split()[1]),
        numbers=list(map(int, numbers.split())),
        winning=list(map(int, winning.split())),
    )


def score(n=0):
    if n < 3:
        return n
    else:
        return 2**(n-1)


def winning_numbers(card):
    return [n for n in card.winning if n in card.numbers]


def task_1_solution(card):
    return score(len(winning_numbers(card)))


class Task2:
    stack = {}

    @staticmethod
    def solution(card):
        result = len(winning_numbers(card))
        multiplier = 1+Task2.stack.get(card.index, 0)
        for n in range(1, result+1):
            index = n+card.index
            Task2.stack[index] = Task2.stack.get(index, 0)+multiplier
        return multiplier


# print(sum(map(task_1_solution, map(parse, sys.stdin))))

print(sum(map(Task2.solution, map(parse, sys.stdin))))

