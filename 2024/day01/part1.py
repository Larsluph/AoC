with open('input.txt', encoding='ascii') as f:
    lines = f.readlines()

left = []
right = []

for line in lines:
    a, b = line.split()
    left.append(int(a))
    right.append(int(b))

left.sort()
right.sort()

total: int = 0
for l, r in zip(left, right):
    total += abs(l - r)

print(total)
