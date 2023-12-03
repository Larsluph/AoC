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

count = 0
for y in vent_map:
    for x in y:
        if x > 1:
            count += 1
print(count)
