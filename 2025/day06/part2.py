from functools import reduce
import operator

with open('input.txt', 'r', encoding='ascii') as f:
    raw_lines = f.readlines()

signs = raw_lines[-1].split()

rotated_text = ['' for _ in range(len(raw_lines[0]))]
for raw_line in raw_lines[:-1]:
    for i, char in enumerate(raw_line.strip('\n')):
        rotated_text[i] += char

with open('input_rotated.txt', 'w', encoding='ascii') as fw:
    fw.write(''.join(map(lambda x: x+'\n', rotated_text)))

problems = []
tmp = []
for rotated_line in rotated_text:
    stripped_line = rotated_line.strip()
    if len(stripped_line) == 0:
        if len(tmp) != 0:
            problems.append(tmp)
            tmp = []
        continue
    tmp.append(int(stripped_line))

assert len(tmp) == 0
assert len(problems) == len(signs)

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
