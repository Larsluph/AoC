from itertools import combinations

with open('input.txt', encoding='ascii') as f:
    lines = f.readlines()

matrix = list(map(lambda line: list(line.strip()), lines))
# for row in matrix:
#     print(*row)

jolts = []

for bank in matrix:
    # print(bank)
    max_value = 0

    # TODO: Optimize for better time efficiency
    for batteries in combinations(bank, 12):
        value = int("".join(batteries))
        max_value = max(max_value, value)

    print(max_value)
    jolts.append(max_value)

print(sum(jolts))
