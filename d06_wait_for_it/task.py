from operator import mul
from functools import reduce
from itertools import chain

from collections import namedtuple
import sys


Race = namedtuple('Race', 'time distance')
Strategy = namedtuple('Strategy', 'button_press distance')


def parse_races(stream):
    times = map(int, stream.readline().split(':')[1].split())
    distances = map(int, stream.readline().split(':')[1].split())
    return [Race(a, b) for a, b in zip(times, distances)]


def margin(race):
    time, distance_record = race
    distances = map(lambda n: Strategy(n, n*(time-n)), range(time+1))
    return [strategy.button_press for strategy in distances if strategy.distance > distance_record]


print(reduce(mul, map(len, map(margin, parse_races(sys.stdin)))))

