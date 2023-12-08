import re

with open('input.txt', encoding='ascii') as f:
    lines = f.readlines()

matrix = list(map(list, map(lambda x: x.strip(), lines)))
matrix_size = (len(matrix[0]), len(matrix))

def is_part(line: int, start: int, end: int) -> bool:
    for y in range(line-1, line+2):
        for x in range(start-1, end+1):
            if x < 0 or x >= matrix_size[0] or y < 0 or y >= matrix_size[1]:
                continue
            elif y == line and start <= x < end:
                continue
            elif (char := matrix[y][x]) != '.' and not char.isdigit():
                return True
    return False

parts = [int(match.group(0))
         for i, line in enumerate(lines)
         for match in re.finditer(r"(\d+)", line)
         if is_part(i, *match.span())]

print(sum(parts))
