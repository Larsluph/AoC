class Entity:
    def __init__(self, id: int | None, type: str, starting_pos: int, size: int) -> None:
        self.id = id
        self.type = type
        self.starting_pos = starting_pos
        self.size = size

    def __repr__(self):
        return f'Block(id={self.id}, type={self.type}, starting_pos={self.starting_pos}, size={self.size})'

def is_file_entity(entity: Entity):
    return entity.type == 'file'

def is_free_entity(entity: Entity):
    return entity.type == 'free'

with open('input.txt', encoding='ascii') as f:
    data = f.read().strip()

next_id = 0
cursor_pos = 0
disk_map: list[Entity] = []
is_file = True
for char in data:
    block_size = int(char)
    if is_file:
        disk_map.append(Entity(id=next_id, type='file', starting_pos=cursor_pos, size=block_size))
        next_id += 1
    is_file = not is_file
    cursor_pos += block_size

# TODO: swap files
