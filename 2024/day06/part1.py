NONE = 0
GUARD = 1
VISITED = 2
OBSTACLE = 3

def cycle_guard_direction(a: tuple[int, int]):
    if a == (0, -1):
        return (1, 0)
    if a == (1, 0):
        return (0, 1)
    if a == (0, 1):
        return (-1, 0)
    if a == (-1, 0):
        return (0, -1)

    raise ValueError('Invalid direction')

area_map = []
guard_pos = (0, 0)
guard_direction = (0, -1)
with open('input.txt', encoding='ascii') as f:
    current_line = []
    cursor_pos = (0, 0)
    for char in f.read():
        if char == '.':
            current_line.append(NONE)
        elif char == '#':
            current_line.append(OBSTACLE)
        elif char == '^':
            guard_pos = cursor_pos
            current_line.append(GUARD)
        elif char == '\n':
            cursor_pos = (-1, cursor_pos[1] + 1)
            area_map.append(current_line)
            current_line = []
        else:
            print('Unknown char:', char)

        cursor_pos = (cursor_pos[0] + 1, cursor_pos[1])

while 0 <= guard_pos[0] < len(area_map[0]) and 0 <= guard_pos[1] < len(area_map):
    x, y = guard_pos
    dx, dy = guard_direction

    try:
        if area_map[y+dy][x+dx] == OBSTACLE:
            dx, dy = guard_direction = cycle_guard_direction(guard_direction)
    except IndexError:
        pass
    else:
        area_map[y+dy][x+dx] = GUARD
    finally:
        area_map[y][x] = VISITED
        guard_pos = (x+dx, y+dy)

print(sum(sum(pos == VISITED for pos in row) for row in area_map))
