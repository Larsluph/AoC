with open('input.txt', encoding='ascii') as f:
    lines = f.readlines()

matrix = list(map(lambda line: list(line.strip()), lines))

jolts = []

NUM_BATTERIES = 12

for bank in matrix:
    n = len(bank)
    result = []
    start = 0
    for i in range(NUM_BATTERIES):
        max_idx = start
        for j in range(start, n - NUM_BATTERIES + i + 1):
            if bank[j] > bank[max_idx]:
                max_idx = j
        result.append(bank[max_idx])
        start = max_idx + 1
    max_value = int("".join(result))

    print(max_value)
    jolts.append(max_value)

print(sum(jolts))
