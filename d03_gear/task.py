from collections import namedtuple
from itertools import chain
import re
import sys


EngineSchematic = namedtuple('EngineSchematic', 'numbers symbols rows cols')
Coordinate = namedtuple('Coordinate', 'index row col')


def within_bounds(schematic, col, row):
    return 0 <= col < schematic.cols and 0 <= row < schematic.rows


def adjacent_indices(element, schematic):
    width = schematic.cols
    offset = width+1
    above = range(element.start-offset-1, element.end-offset+2)
    level = [element.start-1, element.end+1]
    below = range(element.start+offset-1, element.end+offset+2)
    adjacent_coords = [
        Coordinate(index, index // width, index % width)
        for index in chain(above, level, below)
    ]
    return [
        coord.index for coord in adjacent_coords
        if within_bounds(schematic, coord.col, coord.row)
    ]


class SchematicElement:
    PATTERN = None

    def __init__(self, match):
        self.start = match.start()
        self.end = match.end()-1
        self.match = match.group()

    @classmethod
    def matches(cls, blob):
        return list(map(cls, cls.PATTERN.finditer(blob)))


class Number(SchematicElement):
    PATTERN = re.compile(r'\d+', re.MULTILINE)

    def __int__(self):
        return int(self.match)

    def is_part(self, schematic):
        adjacent = adjacent_indices(self, schematic)
        return any(symbol.start in adjacent for symbol in schematic.symbols)


class Symbol(SchematicElement):
    PATTERN = re.compile(r'[^\d\.\n]', re.MULTILINE)

    def __init__(self, match):
        super().__init__(match)
        self.adjacent_numbers = None

    def is_gear(self, schematic):
        if self.adjacent_numbers is None:
            adjacent = set(adjacent_indices(self, schematic))
            self.adjacent_numbers = [
                number for number in schematic.numbers
                if list(adjacent & set(range(number.start, number.end+1)))
            ]
        return len(self.adjacent_numbers) == 2 and self.match == '*'

    @property
    def ratio(self):
        a, b = self.adjacent_numbers
        return int(a) * int(b)


def parse(stream):
    blob = ''.join(stream)
    return EngineSchematic(
        numbers=Number.matches(blob),
        symbols=Symbol.matches(blob),
        rows=len(blob.split('\n')),
        cols=len(blob.split('\n')[0]),
    )


def task_1_solution(schematic):
    return [int(number) for number in schematic.numbers if number.is_part(schematic)]


def task_2_solution(schematic):
    return [gear.ratio for gear in schematic.symbols if gear.is_gear(schematic)]


print(sum(task_2_solution(parse(sys.stdin))))

