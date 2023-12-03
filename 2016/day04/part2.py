from collections import Counter
import re
from larsmod.decryptor import cypher_cesar

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
        decyphered_name = cypher_cesar(room_name, int(sector_id))
        if 'northpole-object-storage' == decyphered_name:
            print(sector_id, decyphered_name)
