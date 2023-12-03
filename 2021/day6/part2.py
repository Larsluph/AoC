from collections import Counter, deque

with open("day6\\input.txt", 'r') as f:
    data = list(map(int, f.read().strip().split(",")))

fishs = Counter(data)
print(fishs)

fishs = deque([fishs[i] for i in range(9)])

for _ in range(256):
    to_reproduce = fishs.popleft()
    fishs.append(to_reproduce)
    fishs[6] += to_reproduce

print(fishs)
print(sum(fishs))
