with open("day7\\input.txt", 'r') as f:
    data = list(map(int, f.read().strip().split(",")))

max_pos = max(data)

least_i = None
least_fuel = None

for pos in range(max_pos):
    total = 0
    for i in data:
        total += abs(i - pos)
    if least_fuel is None or least_fuel > total:
        least_i = pos
        least_fuel = total

print(least_i, least_fuel)
