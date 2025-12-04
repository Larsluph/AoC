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

forklift_accessible_rolls = []
for y, row in enumerate(matrix):
    for x, tile in enumerate(row):
        if tile != '@':
            continue

        if sum(map(lambda char: char == "@", get_safe_rolls(matrix, x, y))) < 4:
            print(f"{x=}, {y=}")
            forklift_accessible_rolls.append((x, y))

print(forklift_accessible_rolls)
print(len(forklift_accessible_rolls))
