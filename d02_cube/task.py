from collections import namedtuple
import sys


GameRecord = namedtuple('GameRecord', 'index rounds')


def parse_round(blob):
    '''e.g. 7 green, 14 red, 5 blue'''
    return {
        color: int(count)
        for count, color in map(str.split, blob.split(','))
    }


def parse_all_rounds(blob):
    '''e.g. 7 green, 14 red, 5 blue; 8 red, 4 green'''
    return map(parse_round, blob.strip().split(';'))


def parse(line):
    '''e.g. Game 1: 7 green, 14 red, 5 blue; 8 red, 4 green'''
    game_blob, rounds_blob = line.strip().split(':')
    return GameRecord(
        index=int(game_blob.split()[1]),
        rounds=parse_all_rounds(rounds_blob),
    )


def possible(round, **limits):
    '''A round is possible if it doesn't exceed the limits'''
    for color, count in round.items():
        if limits[color] < count:
            return False
    return True


def valid(game, **limits):
    '''A game is valid if all its rounds are possible'''
    return all(
        possible(round, **limits)
        for round in game.rounds
    )


def solution(red=0, green=0, blue=0):
    def f(game):
        if valid(game, red=red, green=green, blue=blue):
            return game.index
        else:
            return 0
    return f


print(sum(map(solution(red=12, green=13, blue=14), map(parse, sys.stdin))))

