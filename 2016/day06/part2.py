from collections import Counter

with open('day06\\input.txt') as f:
    lines = f.readlines()

num_columns = len(lines[0].strip())
columns = [str() for _ in range(num_columns)]
for line in lines:
    for i, char in enumerate(line.strip()):
        columns[i] += char

for col in columns:
    c = Counter(col)
    print(c.most_common()[-1][0], end='')
