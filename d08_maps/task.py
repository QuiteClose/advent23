from collections import namedtuple
import sys

# ~~~~~~~~
TASK = 1
# ~~~~~~~~

Node = namedtuple('Node', 'left,right')


def parse_node(line):
    '''e.g. AAA = (BBB, CCC)'''
    name_blob, dir_blob = line.split('=')
    name = name_blob.strip()
    dir_blob = dir_blob.strip()[1:-1]
    left, right = dir_blob.split(', ')
    return name, left, right


def parse(lines):
    instructions = lines.pop(0).strip()
    lines.pop(0)
    nodes = {
        name: Node(left, right)
        for name, left, right in map(parse_node, lines)
    }
    return list(instructions), nodes


def steps(instructions, nodes):
    index = 0
    location = 'AAA'
    while location != 'ZZZ':
        if instructions[index%len(instructions)] == 'L':
            location = nodes[location].left
        else:
            location = nodes[location].right
        index += 1
        yield location


print(len(list(steps(*parse(sys.stdin.readlines())))))
