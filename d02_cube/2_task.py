from collections import namedtuple
from functools import reduce
from operator import mul
import sys


CubeCount = namedtuple('CubeCount', 'count color')
GameRecord = namedtuple('GameRecord', 'index rounds')  # rounds: CubeCount list


def parse_round(s):
    return [
        CubeCount(count=int(count), color=color)
        for count, color in map(lambda s: s.strip().split(), s.split(','))
    ]


def parse(line):
    game_blob, round_blob = line.strip().split(':')
    return GameRecord(
        index=int(game_blob.split()[1]),
        rounds=map(parse_round, round_blob.split(';'))
    )


def fewest(game):
    result = {'red': 0, 'green': 0, 'blue': 0}
    for round in game.rounds:
        for cube in round:
            if result[cube.color] < cube.count:
                result[cube.color] = cube.count
    return result


def power(counts):
    return reduce(mul, counts.values(), 1)


print(sum(map(power, map(fewest, map(parse, sys.stdin)))))

