import re

with open('input.txt', encoding='ascii') as f:
    lines = f.readlines()

matrix = list(map(list, lines))
matrix_size = (len(matrix[0]), len(matrix))

def is_part(line: int, start: int, end: int) -> bool:
    for y in range(line-1, line+2):
        for x in range(start-1, end+2):
            if 0 > x or x >= matrix_size[0] or 0 > y or y >= matrix_size[1] or y == line and start <= x <= end:
                continue
            elif (char := matrix[y][x]) != '.' and not char.isdigit():
                print()
                return True
            print(matrix[y][x], end="")
        print()
    return False

parts = []
for i, line in enumerate(lines):
    for match in re.finditer(r"(\d+)", line):
        value = int(match.group(0))
        span = match.span()
        check = is_part(i, *span)
        print(value, i, span, check)
        if check:
            parts.append(value)

print(sum(parts))
