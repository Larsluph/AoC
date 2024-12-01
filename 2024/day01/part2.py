from collections import Counter

with open('input.txt', encoding='ascii') as f:
    lines = f.readlines()

left = Counter()
right = Counter()

for line in lines:
    a, b = line.split()
    left.update((int(a),))
    right.update((int(b),))

total: int = 0
for l in left:
    total += l * right.get(l, 0)

print(total)
