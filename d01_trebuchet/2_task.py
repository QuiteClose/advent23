import sys

DECIMALS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
NUMBERS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def scan(given):
    '''If the given string STARTS WITH any term in DECIMALS or
    NUMBERS, return the term and its integer value as a tuple.'''
    for source in [DECIMALS, NUMBERS]:
        for term in source:
            if given.startswith(term):
                return term, source.index(term)+1
    return '', None


def to_digits(given):
    digits = []
    while given:
        match, value = scan(given)
        if match:
            digits.append(value)
            given = given[len(match):]
        else:
            given = given[1:]
    return digits


def decode(line):
    digits = to_digits(line)
    return int(str(digits[0])+str(digits[-1]))


print(sum(map(decode, sys.stdin)))

