with open("day5\\input.txt") as f:
    data = f.readlines()

vent_map = [[0 for j in range(1000)] for i in range(1000)]

for line in data:
    xy1, xy2 = line.strip().split(" -> ")
    x1, y1 = tuple(map(int, xy1.split(",")))
    x2, y2 = tuple(map(int, xy2.split(",")))

    # in line (horizontal)
    if x1 == x2:
        y1, y2 = min(y1, y2), max(y1, y2)
        for y in range(y1, y2+1):
            vent_map[y][x1] += 1

    # in line (vertical)
    elif y1 == y2:
        x1, x2 = min(x1, x2), max(x1, x2)
        for x in range(x1, x2+1):
            vent_map[y1][x] += 1

    # in line (diagonal)
    # elif abs(y2-y1) == abs(x2-x1):
    else:
        coef_x = -1 if x1 > x2 else 1
        coef_y = -1 if y1 > y2 else 1
        for x, y in zip(range(x1, x2+coef_x, coef_x), range(y1, y2+coef_y, coef_y)):
            vent_map[y][x] += 1

count = 0
for y in vent_map:
    for x in y:
        if x > 1:
            count += 1
print(count)
