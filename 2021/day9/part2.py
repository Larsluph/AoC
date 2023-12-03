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

def get_adjacent_pos(heightmap: list[list[int]], x: int, y: int) -> tuple:
    size = (len(heightmap[0]), len(heightmap))

    adjacents = list()
    """
      2
    0 x 1
      3
    """

    if x > 0 and heightmap[y][x-1] != 9:
        adjacents.append((x-1, y))
    if x < size[0]-1 and heightmap[y][x+1] != 9:
        adjacents.append((x+1, y))

    if y > 0 and heightmap[y-1][x] != 9:
        adjacents.append((x, y-1))
    if y < size[1]-1 and heightmap[y+1][x] != 9:
        adjacents.append((x, y+1))

    return adjacents

def get_low_points(heightmap: list[list[int]]) -> tuple:
    low_points = tuple()
    for y in range(len(heightmap)):
        for x in range(len(heightmap[0])):
            cur, adjacents = get_adjacents(heightmap, x, y)
            if all([cur < adjacent for adjacent in adjacents]):
                low_points += ((x, y),)
    return low_points

def get_basins(heightmap):
    basins = list()
    low_points = get_low_points(heightmap)
    for low_point in low_points:
        basin = [low_point]
        adjacents = get_adjacent_pos(heightmap, *low_point)
        i = 0
        while i < len(adjacents):
            adjacent = x, y = adjacents[i]
            if heightmap[y][x] != 9:
                if adjacent not in basin:
                    basin.append(adjacent)
                for adj in get_adjacent_pos(heightmap, *adjacent):
                    if adj not in adjacents:
                        adjacents.append(adj)
            i += 1
        basins.append(len(basin))
    return sorted(basins, reverse=True)

with open("day9\\input.txt", 'r') as f:
    data = list(map(lambda x: list(map(int, x)), f.read().splitlines()))

basins = get_basins(data)
print(basins)
print(basins[0]*basins[1]*basins[2])
