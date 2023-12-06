from operator import mul
from functools import reduce

from collections import namedtuple
import sys


Race = namedtuple('Race', 'time distance')
Strategy = namedtuple('Strategy', 'button_press distance')


def race_strategy(button_press, time):
    return Strategy(button_press, button_press*(time-button_press))


def winning(distance, strategy):
    return strategy.distance > distance


def shortest_button_press(race):
    lower = 1
    upper = race.time//2
    while True:
        probe = (upper+lower)//2
        strategy = race_strategy(probe, race.time)
        if winning(race.distance, strategy):
            shorter_press = race_strategy(probe-1, race.time)
            if not winning(race.distance, shorter_press):
                return strategy.button_press
            upper = strategy.button_press-1
        else:
            lower = strategy.button_press+1


def longest_button_press(race):
    lower = race.time//2
    upper = race.time
    while True:
        probe = (upper+lower)//2
        strategy = race_strategy(probe, race.time)
        if winning(race.distance, strategy):
            longer_press = race_strategy(probe+1, race.time)
            if not winning(race.distance, longer_press):
                return strategy.button_press
            lower = strategy.button_press+1
        else:
            upper = strategy.button_press-1


def parse_races_task_one(stream):
    times = map(int, stream.readline().split(':')[1].split())
    distances = map(int, stream.readline().split(':')[1].split())
    return [Race(a, b) for a, b in zip(times, distances)]


def parse_races_task_two(stream):
    time = int(''.join(stream.readline().split(':')[1].split()))
    distance = int(''.join(stream.readline().split(':')[1].split()))
    return Race(time, distance)


def margin(race):
    return range(shortest_button_press(race), longest_button_press(race)+1)


def margin_search(race):
    return longest_button_press(race)-shortest_button_press(race)+1


# print(reduce(mul, map(len, map(margin, parse_races_task_one(sys.stdin)))))
print(margin_search(parse_races_task_two(sys.stdin)))

