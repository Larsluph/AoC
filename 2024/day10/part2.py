from collections import Counter

def follow_trail(max_height: int, next_height: int, cursor: tuple[int, int], past_results: Counter):
    for x, y in ((-1, 0),
                 (0, -1),
                 (1, 0),
                 (0, 1)):
        new_x, new_y = cursor[0] + x, cursor[1] + y

        if 0 > new_x or new_x >= len(topo_map) or 0 > new_y or new_y >= len(topo_map):
            continue

        new_height = topo_map[new_y][new_x]
        if new_height == next_height:
            if new_height == max_height:
                print(f'Found complete trail on tile ({new_x}, {new_y})')
                past_results.update([(new_x, new_y)])
                continue
            print(f'Found next height on tile ({new_x}, {new_y}): {new_height}')
            follow_trail(max_height,
                         next_height + 1,
                         (new_x, new_y),
                         past_results)
    print('<< END', next_height)


with open('input.txt', encoding='ascii') as f:
    topo_map = [list(map(int, line.strip())) for line in f.readlines()]

trails = Counter()
for j, row in enumerate(topo_map):
    for i, digit in enumerate(row):
        if digit == 0:
            trail_head = (i, j)
            print('=============')
            print(f'Found trail head on tile {trail_head}')
            follow_trail(9, 1, trail_head, trails)

print(trails.total())
