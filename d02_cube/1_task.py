import sys
from collections import namedtuple

LIMITS = {
   'red': 12,
   'green': 13,
   'blue': 14
}


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


def rounds_possible(round, red, green, blue):
    for color, count in [('red', red), ('green', green), ('blue', blue)]:
        for cube in round:
            if cube.color == color and cube.count > count:
                return False
    return True


def possible(red=0, green=0, blue=0):
    def f(game):
        if all(rounds_possible(round, red, green, blue) for round in game.rounds):
            return game.index
        else:
            return 0
    return f


print(sum(map(possible(**LIMITS), map(parse, sys.stdin))))

