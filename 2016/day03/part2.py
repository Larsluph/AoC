from numpy import array

with open('day03\\input.txt') as f:
    triangles = f.readlines()
sides = [tuple(map(int, filter(lambda x: x != '', triangle.strip().split(' ')))) for triangle in triangles]

data = array(sides).reshape(-1, 3).transpose().reshape(-1, 3)

count = 0
for sides in data:
    max_side = max(sides)
    other_sides = sum(sides) - max_side
    if max_side < other_sides:
        count += 1

print(count)
