from collections import namedtuple
from itertools import chain
import re
import sys


EngineSchematic = namedtuple('EngineSchematic', 'numbers symbols rows cols')


class SchematicElement:
    PATTERN = None

    def __init__(self, match):
        self.start = match.start()
        self.end = match.end()-1
        self.match = match.group()

    def __str__(self):
        return '{}(start={}, end={}, match={})'.format(
            self.__class__.__name__,
            self.start,
            self.end,
            self.match,
        )

    def __repr__(self):
        return f'{self.__class__.__name__}({self.match})'


class Number(SchematicElement):
    PATTERN = re.compile(r'\d+', re.MULTILINE)

    def __int__(self):
        return int(self.match)


class Symbol(SchematicElement):
    PATTERN = re.compile(r'[^\d\.\n]', re.MULTILINE)


def parse(stream):
    blob = ''.join(stream)
    return EngineSchematic(
        numbers=list(map(Number, Number.PATTERN.finditer(blob))),
        symbols=list(map(Symbol, Symbol.PATTERN.finditer(blob))),
        rows=len(blob.split('\n')),
        cols=len(blob.split('\n')[0]),
    )


def is_part(number, schematic):
    width = schematic.cols
    offset = width+1
    above = range(number.start-offset-1, number.end-offset+2)
    level = [number.start-1, number.end+1]
    below = range(number.start+offset-1, number.end+offset+2)
    adjacent_coords = list(map(
        lambda index: (index, index//width, index%width),
        chain(above, level, below),
    ))
    adjacent = [
        coord[0] for coord in adjacent_coords
        if 0 <= coord[1] < schematic.cols and 0 <= coord[2] < schematic.rows
    ]
    return any(symbol.start in adjacent for symbol in schematic.symbols)


def solution(schematic):
    return [int(number) for number in schematic.numbers if is_part(number, schematic)]


print(sum(solution(parse(sys.stdin))))

