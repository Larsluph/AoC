from collections import Counter
import re

with open('day04\\input.txt') as f:
    data = f.readlines()

room_pattern = re.compile(r'([\w-]+)-(\d+)\[(\w+)\]')

global_sum = 0
for room_id in data:
    room_name, sector_id, checksum = room_pattern.match(room_id).groups()
    c = Counter(room_name.replace('-', ''))
    letters_occurs = list(c.items())
    letters_occurs.sort(key=lambda x: (x[1], -ord(x[0])), reverse=True)
    if checksum == "".join(map(lambda x: x[0], letters_occurs[:5])):
        global_sum += int(sector_id)
print(global_sum)
