from collections import defaultdict
from typing import Literal


with open('input_test.txt', encoding='ascii') as f:
    garden_plots = list(map(lambda x: list(x.strip()), f.readlines()))

parsed_plots = set()
all_regions: defaultdict[str, list[set[tuple[int, int]]]] = defaultdict(list)

directions = [
    (-1, 0),  # left
    (1, 0),   # right
    (0, -1),  # up
    (0, 1),   # down
]

HORIZONTAL = 1
VERTICAL = 2


def safe_garden_plot(x: int, y: int):
    if 0 <= x < len(garden_plots) and 0 <= y < len(garden_plots):
        return garden_plots[y][x]
    return None


def walk_region(acc: set[tuple[int, int]], x: int, y: int):
    if (x, y) in parsed_plots:
        return

    parsed_plots.add((x, y))
    acc.add((x, y))

    for dx, dy in directions:
        new_x, new_y = x+dx, y+dy
        if safe_garden_plot(new_x, new_y) == garden_plots[y][x]:
            acc.add((new_x, new_y))
            walk_region(acc, x+dx, y+dy)


def calc_perimeter(x: int, y: int):
    perimeter: set[tuple[Literal[1, 2], tuple[int, int]]] = set()
    for dx, dy in directions:
        if safe_garden_plot(x+dx, y+dy) != garden_plots[y][x]:
            perimeter.add(
                (abs(dy)*HORIZONTAL + abs(dx)*VERTICAL, (x + ((dx+1)//2), y + ((dy+1)//2))))
    return perimeter


for j, row in enumerate(garden_plots):
    for i, plot in enumerate(row):
        current_region = set()
        walk_region(current_region, i, j)
        if len(current_region) > 0:
            all_regions[plot].append(current_region)

total = 0
for k, regions in all_regions.items():
    print(k)
    for region in regions:
        region_sides = set()
        for i, j in region:
            region_sides |= calc_perimeter(i, j)
        sides = sorted(region_sides, key=lambda x: (
            x[0], x[1][1 if x[0] == HORIZONTAL else 0], x[1][1 if x[0] == VERTICAL else 0]))

        # TODO: Group sides

        print(len(region), region)
        print("XX", len(region_sides), region_sides)
        # total += len(region) * region_perimeter
    print("========")

print(total)
