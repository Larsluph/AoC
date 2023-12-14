import re
from typing import List, Tuple
from collections import deque

with open('input.txt', encoding='ascii') as f:
    lines = f.readlines()

matrix = list(map(list, map(lambda x: x.strip(), lines)))
matrix_size = (len(matrix[0]), len(matrix))


def check_part(x: int, y: int) -> Tuple[bool, List[Tuple[int, int]]]:
    part_numbers = list()
    for yi in range(y-1, y+2):
        part_detected = False
        for xi in range(x-1, x+2):
            if xi < 0 or xi >= matrix_size[0] or yi < 0 or yi >= matrix_size[1]:
                part_detected = False  # OOB
            elif yi == y and xi == x:
                part_detected = False  # Skip targeted char
            elif matrix[yi][xi].isdigit():
                if not part_detected:
                    part_numbers.append((xi, yi))
                    part_detected = True
                else:
                    continue # Already registered part number
            else:
                part_detected = False
    return len(part_numbers) == 2, part_numbers


def get_part_number(*values: List[Tuple[int, int]]):
    print(values)
    total = 1
    for x, y in values:
        part_number = deque()
        # Expand left
        xi = x
        while xi >= 0 and (char := matrix[y][xi]).isdigit():
            part_number.appendleft(char)
            xi -= 1
        # Expand right
        xi = x+1
        while xi < matrix_size[0] and (char := matrix[y][xi]).isdigit():
            part_number.append(char)
            xi += 1
        print(part_number)
        total *= int("".join(part_number))
    print(total)
    print("=========")
    return total

parts = []
for i, line in enumerate(lines):
    for match in re.finditer(r"\*", line):
        parts.append(check_part(match.start(), i))

filtered_parts = filter(lambda x: x[0], parts)

print(sum(map(lambda x: get_part_number(*x[1]), filtered_parts)))
