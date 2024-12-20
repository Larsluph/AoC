from collections import Counter

class Block:
    def __init__(self, id: int | None, type: str, pos: int) -> None:
        self.id = id
        self.type = type
        self.pos = pos

    def __repr__(self):
        return f'Block(id={self.id}, type={self.type}, pos={self.pos})'

def is_file_block(block: Block) -> bool:
    return block.type == 'file'

def is_free_block(block: Block) -> bool:
    return block.type == 'free'

def first_free_block(size: int):
    pos = 0
    contiguous = 0
    for i, block in enumerate(disk_map):
        if is_file_block(block):
            contiguous = 0
        else:
            if contiguous == 0:
                pos = i
            contiguous += 1

        if contiguous == size:
            return pos
    return None

with open('input.txt', encoding='ascii') as f:
    data = f.read().strip()

file_sizes = Counter()
next_id = 0
cursor_pos = 0
disk_map: list[Block] = []
is_file = True
for char in data:
    block_size = int(char)
    for i in range(block_size):
        if is_file:
            file_sizes.update([next_id])
            disk_map.append(Block(id=next_id, type='file', pos=cursor_pos + i))
        else:
            disk_map.append(Block(id=None, type='free', pos=cursor_pos + i))
    if is_file:
        next_id += 1
    is_file = not is_file
    cursor_pos += block_size

loop = True
while loop:
    loop = False

    for block in filter(is_file_block, reversed(disk_map)):
        file_size = file_sizes.get(block.id, -1)
        if (first_free_pos := first_free_block(file_size)) is None:
            continue

        loop = True
        # for i in range(file_size):
        #     file_block, free_block = disk_map[first_free_pos + i], disk_map[block.pos - i] = disk_map[block.pos - i], disk_map[first_free_pos + i]
        #     free_block.pos = file_block.pos - i
        #     file_block.pos = first_free_pos + i
        # break

total = 0
debug = list('.' * len(disk_map))
for i, block in enumerate(disk_map):
    if debug[block.pos] == 'X':
        print('!!!!!!')

    if block.type == 'file':
        debug[block.pos] = 'X'
        total += block.id * block.pos

sorted_disk_map = sorted(disk_map, key=lambda x: x.pos)

print(''.join(debug))
print(total)
