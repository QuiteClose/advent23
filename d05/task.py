
from collections import namedtuple
from functools import partial
import sys


Mapping = namedtuple('Mapping', 'destination source magnitude')


def read_until_empty_line(stream):
    blob = []
    for line in stream:
        line = line.strip()
        if line:
            blob.append(line)
        else:
            break
    return blob


def read_seeds_task_one(stream):
    blob = read_until_empty_line(stream)
    _, numbers = blob[0].split(':')
    return [int(n) for n in numbers.strip().split()]


def parse_line(line):
    destination, source, magnitude = line.strip().split()
    return Mapping(int(destination), int(source), int(magnitude))


def read_sections(stream):
    while True:
        blob = read_until_empty_line(stream)
        if not blob:
            return
        blob.pop(0)
        yield list(map(parse_line, blob))


def transform_one(mapping, n):
    for destination, source, magnitude in mapping:
        if source <= n < source+magnitude:
            return destination+(n-source)
    return n


def solution(stream, *data):
    for mapping in read_sections(stream):
        transform = partial(transform_one, mapping)
        data = map(transform, data)
    return sorted(data)[0]


def task_one(stream):
    seeds = read_seeds_task_one(stream)
    return solution(stream, *seeds)


print(task_one(sys.stdin))

