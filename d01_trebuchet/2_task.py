import sys

DECIMALS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
NUMBERS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def scan(given):
    '''If the given string STARTS WITH any term in DECIMALS or
    NUMBERS, return a single-character string of that term.'''
    for source in [DECIMALS, NUMBERS]:
        for term in source:
            if given.startswith(term):
                return str(source.index(term)+1)


def to_digits(given):
    digits = []
    while given:
        match = scan(given)
        if match:
            digits.append(match)
        given = given[1:]
    return digits


def decode(line):
    digits = to_digits(line)
    return int(digits[0]+digits[-1])


print(sum(map(decode, sys.stdin)))

