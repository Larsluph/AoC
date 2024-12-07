from functools import reduce
from itertools import product

def parse_line(line: str):
    res, ops = line.split(': ')
    return int(res), list(map(int, ops.split()))

def equation_reducer(acc: int, curr):
    d, op = curr

    if op == ADD:
        return acc + d
    if op == MULTIPLY:
        return acc * d
    raise ValueError('Unknown operator', op)

with open('input.txt', encoding='ascii') as f:
    equations = [parse_line(line) for line in f.readlines()]

ADD = 1
MULTIPLY = 2

total = 0
for result, operands in equations:
    for combination in product((ADD, MULTIPLY), repeat=len(operands)-1):
        if result == reduce(equation_reducer, zip(operands[1:], combination), operands[0]):
            # print(result, operands, combination)
            total += result
            break

print(total)
