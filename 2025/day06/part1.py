from functools import reduce
import operator

with open('input.txt', 'r', encoding='ascii') as f:
    raw_lines = f.readlines()

signs = raw_lines[-1].split()

problems = [list() for _ in range(len(signs))]
for raw_line in raw_lines[:-1]:
    line = map(int, raw_line.strip().split())
    for i, number in enumerate(line):
        problems[i].append(number)

def get_acc_from_sign(sign: str):
    match sign:
        case '+':
            return operator.add, 0
        case '*':
            return operator.mul, 1
        case _:
            print(f"Unknown sign: {sign}")
            return None

def fixed_reduce(acc, base, problem):
    return reduce(acc, problem, base)

solved_problems = [fixed_reduce(*get_acc_from_sign(sign), problem) for sign, problem in zip(signs, problems)]

#print(problems)
#print(solved_problems)
print(sum(solved_problems))
