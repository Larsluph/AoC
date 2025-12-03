with open('input.txt', encoding='ascii') as f:
    lines = f.readlines()

matrix = list(map(lambda line: list(line.strip()), lines))

jolts = []

for bank in matrix:
    max_value = 0
    for i in range(len(bank)-1):
        for j in range(i+1, len(bank)):
            value = int(bank[i] + bank[j])
            max_value = max(max_value, value)
    jolts.append(max_value)

print(sum(jolts))
