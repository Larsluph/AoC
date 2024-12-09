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

with open('input.txt', encoding='ascii') as f:
    data = f.read().strip()

next_id = 0
cursor_pos = 0
disk_map: list[Block] = []
is_file = True
for char in data:
    block_size = int(char)
    for i in range(block_size):
        if is_file:
            disk_map.append(Block(id=next_id, type='file', pos=cursor_pos + i))
        else:
            disk_map.append(Block(id=None, type='free', pos=cursor_pos + i))
    if is_file:
        next_id += 1
    is_file = not is_file
    cursor_pos += block_size

for file, free in zip(reversed(list(filter(is_file_block, disk_map))), filter(is_free_block, disk_map)):
    if file.pos < free.pos:
        break

    file.pos, free.pos = free.pos, file.pos

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
