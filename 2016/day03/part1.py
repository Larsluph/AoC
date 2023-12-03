with open('day03\\input.txt') as f:
    triangles = f.readlines()

count = 0
for triangle in triangles:
    sides = tuple(map(int, filter(lambda x: x != '', triangle.strip().split(' '))))
    max_side = max(sides)
    other_sides = sum(sides) - max_side
    if max_side < other_sides:
        count += 1

print(count)
