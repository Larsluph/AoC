with open('input.txt', 'r', encoding='ascii') as f:
    lines = f.readlines()

matrix = list(map(lambda line: list(line.strip()), lines))

deltas = (
    (-1, -1),  # top-left
    (0, -1),   # up
    (1, -1),   # top-right
    (-1, 0),   # left
    (1, 0),    # right
    (-1, 1),   # bottom-left
    (0, 1),    # down
    (1, 1),    # bottom-right
)

def get_safe_rolls(mat, x, y):
    for dx,dy in deltas:
        ddx = x+dx
        ddy = y+dy
        if ddx < 0 or ddx >= len(mat[0]):
            yield None

        elif ddy < 0 or ddy >= len(mat):
            yield None

        else:
            yield mat[ddy][ddx]

def run_roll_check(mat):
    forklift_accessible_rolls = []
    for y, row in enumerate(mat):
        for x, tile in enumerate(row):
            if tile != '@':
                continue

            if sum(map(lambda char: char == "@", get_safe_rolls(mat, x, y))) < 4:
                # print(f"{x=}, {y=}")
                forklift_accessible_rolls.append((x, y))
    return forklift_accessible_rolls

last_check = -1
forklift_accessible_rolls = []
while last_check != 0:
    removed_rolls = run_roll_check(matrix)
    forklift_accessible_rolls.extend(removed_rolls)
    for rx, ry in removed_rolls:
        matrix[ry][rx] = '.'
    last_check = len(removed_rolls)
    print(f"Removed {last_check} rolls")

print(forklift_accessible_rolls)
print(len(forklift_accessible_rolls))
