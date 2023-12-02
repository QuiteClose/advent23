import sys

DECIMALS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
NUMBERS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def scan(given):
    '''If the given string starts with any term in DECIMALS or
    NUMBERS, return the term and the source list as a tuple.'''
    for source in [DECIMALS, NUMBERS]:
        for term in source:
            if given.startswith(term):
                return term, source
    return '', None


def to_digits(given, digits=None):
    if digits is None:
        digits = []
    if not given:
        return digits
    match, source = scan(given)
    if match:
        digits.append(str(source.index(match)+1))
        return to_digits(given[len(match):], digits)
    else:
        return to_digits(given[1:], digits)


def decode(line):
    digits = to_digits(line)
    result = int(digits[0]+digits[-1])
    return result


print(sum(map(decode, sys.stdin)))

