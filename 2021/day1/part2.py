from collections import deque

with open("day1\\input.txt", 'r') as f:
    depths = f.readlines()

queue = deque(maxlen=4)

count_increase = 0

for i in range(len(depths)):
    queue.append(int(depths[i][:-1]))
    if len(queue) < 4:
        continue
    
    vals = list(queue)
    if sum(vals[1:]) > sum(vals[:3]):
        count_increase += 1

print(count_increase)
