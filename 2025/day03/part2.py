with open('input.txt', encoding='ascii') as f:
    lines = f.readlines()

matrix = list(map(lambda line: list(line.strip()), lines))
# for row in matrix:
#     print(*row)

jolts = []

NUM_BATTERIES = 12

for bank in matrix:
    # print(bank)

    # Greedy selection: pick the largest digit at each position
    # while ensuring enough digits remain for subsequent positions
    # Note: String comparison works correctly for single digit characters ('0'-'9')
    n = len(bank)
    result = []
    start = 0
    for i in range(NUM_BATTERIES):
        end = n - NUM_BATTERIES + i + 1
        max_idx = start
        for j in range(start, end):
            if bank[j] > bank[max_idx]:
                max_idx = j
        result.append(bank[max_idx])
        start = max_idx + 1
    max_value = int("".join(result))

    print(max_value)
    jolts.append(max_value)

print(sum(jolts))
