from typing import List, Optional

class TreeNodeType:
    DIRECTORY = "dir"
    FILE = "file"

class TreeNode:
    parent: Optional["TreeNode"]
    content: List["TreeNode"]
    type: TreeNodeType
    name: str
    size: Optional[int]

    def __init__(self,
                 parent = None,
                 content = None,
                 type = None,
                 name = None,
                 size = None) -> None:
        self.parent = parent if parent else None
        self.content = content if content else list()
        self.type = type if type else None
        self.name = name if name else None
        self.size = size if size else None

    def __str__(self):
        return f"<TreeNode name='{self.name}' type='{self.type}'>"
    __repr__ = __str__

    @property
    def total_size(self):
        if self.type == TreeNodeType.FILE:
            return self.size
        else:
            return sum(map(lambda entry: entry.total_size, self.content))

    def find(self, name: str):
        for child in current_node.content:
            if child.name == name:
                return child

    def walk_directories(self):
        for child in self.content:
            if child.type == TreeNodeType.DIRECTORY:
                yield child
                yield from child.walk_directories()

root = TreeNode(name='/', type=TreeNodeType.DIRECTORY)
current_node: TreeNode
with open('input.txt', 'r') as f:
    for line in f.readlines():
        if line.startswith("$ cd "):
            next_hop = line.strip()[5:]
            if next_hop == "/":
                current_node = root
                continue
            elif next_hop == "..":
                current_node = current_node.parent
                continue
            else:
                node = current_node.find(next_hop)
                if node is None:
                    breakpoint()
                else:
                    current_node = node
                    continue
        elif line.strip() == "$ ls":
            continue
        else:
            # in ls command
            type, name = line.strip().split(' ')
            node = TreeNode(parent=current_node, name=name)
            current_node.content.append(node)
            if type == "dir":
                node.type = TreeNodeType.DIRECTORY
            elif type.isdigit():
                node.type = TreeNodeType.FILE
                node.size = int(type)

CAPACITY = 70_000_000
TARGET = 30_000_000
NEEDED = TARGET - (CAPACITY - root.total_size)

candidates: List[TreeNode] = list()
for child in root.walk_directories():
    size = child.total_size
    if size >= NEEDED:
        candidates.append(child)

min = candidates[0].total_size
for node in candidates:
    size = node.total_size
    if size < min:
        min = size

print(min)
