
from collections import namedtuple
import sys


Mapping = namedtuple('Mapping', 'destination source magnitude')
ValueRange = namedtuple('ValueRange', 'start end magnitude')


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
    '''e.g. seeds: 79 14 55 13'''
    blob = read_until_empty_line(stream)
    _, numbers = blob[0].split(':')
    return [int(n) for n in numbers.strip().split()]


def chunks(iterable, size):
    for i in range(0, len(iterable), size):
        yield iterable[i:i+size]


def read_seeds_task_two(stream):
    '''e.g. seeds: 79 14 55 13'''
    numbers = read_seeds_task_one(stream)
    while 
    return [
        ValueRange(start, start+magnitude, magnitude)
        for start, magnitude in chunks(read_seeds_task_one(stream), 2)
    ]


def parse_line(line):
    destination, source, magnitude = line.strip().split()
    return Mapping(int(destination), int(source), int(magnitude))


def read_sections(stream):
    while True:
        blob = read_until_empty_line(stream)
        if not blob:
            return
        print(blob.pop(0))
        yield list(map(parse_line, blob))


def transform_one(mapping, n):
    for destination, source, magnitude in mapping:
        if source <= n < source+magnitude:
            return destination+(n-source)
    return n


def transform_range(mapping, value_range):
    index = value_range.start
    for destination, source, magnitude in sorted(mapping, key=lambda x: x.source):
        offset = destination-source
        if index < source and value_range.end < source:
            yield ValueRange(index, value_range.end, value_range.end-index)
            return
        elif index < source and source < value_range.end <= source+magnitude:
            yield ValueRange(index, source, source-index)
            yield ValueRange(
                source+offset,
                value_range.end+offset,
                value_range.end-source,
            )
            return
        elif index < source and value_range.end >= source+magnitude:
            yield ValueRange(index, source, source-index)
            yield ValueRange(
                source+offset,
                source+magnitude+offset,
                magnitude,
            )
            index = source+magnitude
        elif source <= index < source+magnitude and value_range.end <= source+magnitude:
            yield ValueRange(
                index+offset,
                value_range.end+offset,
                value_range.end-index,
            )
            return
        elif source <= index < source+magnitude and value_range.end > source+magnitude:
            yield ValueRange(
                index+offset,
                source+magnitude+offset,
                source+magnitude-index,
            )
            index = source+magnitude
    else:
        yield ValueRange(index, value_range.end, value_range.end-index)


def task_one(stream):
    data = read_seeds_task_one(stream)
    for mapping in read_sections(stream):
        data = transform_one(mapping, data)
    return sorted(data)[0]


def task_two_solution(mapping, data):
    result = []
    for value_range in data:
        for output in transform_range(mapping, value_range):
            result.append(output)
    return result


def task_two(stream):
    data = read_seeds_task_two(stream)
    for mapping in read_sections(stream):
        data = task_two_solution(mapping, data)
    return sorted(data, key=lambda x: x.start)[0].start


# print(task_one(sys.stdin))
print(task_two(sys.stdin))

