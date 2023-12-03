def get_adjacents(heightmap: list[list[int]], x: int, y: int) -> tuple:
    size = (len(heightmap[0]), len(heightmap))

    adjacents = tuple()
    """
      2
    0 x 1
      3
    """

    if x > 0:
        adjacents += (heightmap[y][x-1], )
    if x < size[0]-1:
        adjacents += (heightmap[y][x+1], )

    if y > 0:
        adjacents += (heightmap[y-1][x], )
    if y < size[1]-1:
        adjacents += (heightmap[y+1][x], )

    return heightmap[y][x], adjacents

def get_low_points(heightmap: list[list[int]]) -> tuple:
    low_points = tuple()
    for y in range(len(heightmap)):
        for x in range(len(heightmap[0])):
            cur, adjacents = get_adjacents(heightmap, x, y)
            if all([cur < adjacent for adjacent in adjacents]):
                low_points += ((x, y),)
    return low_points

def get_risk_level(heightmap: list[list[int]]):
    res = 0
    for x, y in get_low_points(heightmap):
        res += heightmap[y][x] + 1
    return res

with open("day9\\input.txt", 'r') as f:
    data = list(map(lambda x: list(map(int, x)), f.read().splitlines()))

print(get_risk_level(data))
