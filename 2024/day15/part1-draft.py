from abc import abstractmethod
from enum import Enum, auto

class Direction(Enum):
    LEFT = auto()
    RIGHT = auto()
    UP = auto()
    DOWN = auto()

    @property
    def delta(self):
        match self:
            case Direction.LEFT:
                return (-1, 0)
            case Direction.RIGHT:
                return (1, 0)
            case Direction.UP:
                return (0, -1)
            case Direction.DOWN:
                return (0, 1)
            case val:
                raise ValueError(val)


class Tile:
    _map: "Map"

    def __init__(self, parent_map: "Map"):
        self._map = parent_map

    @abstractmethod
    def __str__(self):
        raise NotImplementedError

    def __repr__(self):
        return f'<{self.__class__.__name__}>'


class Air(Tile):
    def __str__(self):
        return ' '


class Wall(Tile):
    def __str__(self):
        return '#'


class Box(Tile):
    def __str__(self):
        return 'O'


class Robot(Tile):
    def __str__(self):
        return '@'


class Map:
    _map: list[list[Tile]]
    _instructions: list[Direction]
    robot_pos: tuple[int, int]

    def __init__(self) -> None:
        self._map = []
        self._instructions = []
        self.robot_pos = (-1, -1)

    def append_line(self, line: str):
        row = []
        j = len(self._map)
        for i, char in enumerate(line.strip()):
            match char:
                case '#':
                    row.append(Wall(self))
                case 'O':
                    row.append(Box(self))
                case '@':
                    self.robot_pos = (i, j)
                    row.append(Robot(self))
                case '.':
                    row.append(Air(self))
                case val:
                    raise ValueError(val)
        self._map.append(row)

    def append_instructions(self, line: str):
        for instruction in line:
            match instruction:
                case '<':
                    self._instructions.append(Direction.LEFT)
                case '>':
                    self._instructions.append(Direction.RIGHT)
                case '^':
                    self._instructions.append(Direction.UP)
                case 'v':
                    self._instructions.append(Direction.DOWN)
                case val:
                    raise ValueError(val)

    def render_map(self):
        for row in self._map:
            print(*map(str, row), sep='')

    def lookup_tile(self, x: int, y: int):
        if 0 <= x < len(self._map[0]) and 0 <= y < len(self._map):
            return self._map[y][x]
        return None

    def exec_1_step(self, x: int, y: int, direction: Direction):
        dx, dy = direction.delta
        new_x, new_y = x+dx, y+dy
        tile = self.lookup_tile(new_x, new_y)
        if isinstance(tile, Air):
            self._map[y][x], self._map[new_y][new_x] = self._map[new_y][new_x], self._map[y][x]
            return True
        elif isinstance(tile, Wall):
            return False
        elif isinstance(tile, Box):
            self.exec_1_step(new_x, new_y, direction)
            # self.exec_1_step(x, y, direction)
            return True
        else:
            raise ValueError(tile)

    def exec(self):
        for instruction in self._instructions:
            x, y = self.robot_pos
            if self.exec_1_step(x, y, instruction):
                dx, dy = instruction.delta
                self.robot_pos = x+dx, y+dy
            self.render_map()


warehouse_map = Map()

with open('input.txt', encoding='ascii') as f:
    detect_map = True
    for l in f.readlines():
        if l == '\n':
            detect_map = False
            continue

        (warehouse_map.append_line if detect_map else warehouse_map.append_instructions)(
            l.strip())

warehouse_map.exec()
