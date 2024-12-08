from collections import defaultdict
from itertools import combinations


def check_oob(a: int, b: int):
    return a < 0 or a >= mat_size[0] or b < 0 or b >= mat_size[1]


antenna_locations = defaultdict(list)
mat_size = (0, 0)
with open('input.txt', encoding='ascii') as f:
    for y, line in enumerate(map(lambda x: x.strip(), f.readlines())):
        mat_size = (len(line), mat_size[1] + 1)
        for x, char in enumerate(line):
            if char in ('.', '\n'):
                continue
            antenna_locations[char].append((x, y))

antinode_locations = set()
for k, v in antenna_locations.items():
    for comb in combinations(v, 2):
        (x1, y1), (x2, y2) = comb
        dx, dy = x2 - x1, y2 - y1

        expected_coords = [(x1 - k*dx, y1 - k*dy) for k in range(50)] + \
                          [(x1 + k*dx, y1 + k*dy) for k in range(50)] + \
                          [(x2 - k*dx, y2 - k*dy) for k in range(50)] + \
                          [(x2 + k*dx, y2 + k*dy) for k in range(50)]

        for coords in expected_coords:
            if check_oob(*coords):
                continue

            antinode_locations.add(coords)

print(antinode_locations)
print(len(antinode_locations))
