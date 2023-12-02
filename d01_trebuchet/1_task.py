import sys


def decode(line):
    digits = list(filter(str.isdigit, line))
    return int(digits[0]+digits[-1])


print(sum(map(decode, sys.stdin)))

