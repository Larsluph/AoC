from itertools import count
import re


robot_pattern = re.compile(
    r'p=(?P<px>\d+),(?P<py>\d+) v=(?P<vx>-?\d+),(?P<vy>-?\d+)')


class Robot:
    initial_x: int
    initial_y: int
    velocity_x: int
    velocity_y: int

    def __init__(self, properties: str) -> None:
        result = robot_pattern.match(properties)
        assert result is not None
        self.initial_x = int(result.group('px'))
        self.initial_y = int(result.group('py'))
        self.velocity_x = int(result.group('vx'))
        self.velocity_y = int(result.group('vy'))

    def __repr__(self):
        return 'Robot<'\
            f'pos=({self.initial_x},{self.initial_y}), '\
            f'velocity={self.velocity_x},{self.velocity_y}'\
            '>'

    def predict_position(self, seconds: int, borders: tuple[int, int]):
        return (
            (self.initial_x + self.velocity_x*seconds) % borders[0],
            (self.initial_y + self.velocity_y*seconds) % borders[1]
        )


with open('input.txt', encoding='ascii') as f:
    robots = list(map(Robot, f.readlines()))

map_x, map_y = map_size = (101, 103)

for i in count():
    check = False
    current_map = [[' ' for _ in range(map_x)] for _ in range(map_y)]
    for robot in robots:
        hat_x, hat_y = robot.predict_position(i, map_size)
        current_map[hat_y][hat_x] = 'X'

    for row in current_map:
        if 'X'*10 in ''.join(row):
            check = True

    if i % 1000 == 0:
        print(i)

    if check:
        print('\n'.join(''.join(row) for row in current_map))
        input(i)
        break
