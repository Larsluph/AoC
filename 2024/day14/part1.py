from functools import reduce
from math import floor
from operator import mul
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
quad_x_bound = floor(map_x / 2)
quad_y_bound = floor(map_y / 2)
quadrants = [0, 0, 0, 0]
skipped = 0

for robot in robots:
    hat_x, hat_y = robot.predict_position(100, map_size)
    if hat_x == quad_x_bound or hat_y == quad_y_bound:
        skipped += 1
        continue

    if hat_x < quad_x_bound and hat_y < quad_y_bound:
        # top-left
        quadrants[0] += 1
    elif hat_x > quad_x_bound and hat_y < quad_y_bound:
        # top-right
        quadrants[1] += 1
    elif hat_x < quad_x_bound and hat_y > quad_y_bound:
        # bottom-left
        quadrants[2] += 1
    elif hat_x > quad_x_bound and hat_y > quad_y_bound:
        # bottom-right
        quadrants[3] += 1
    else:
        print('!!!!!!!')

print(skipped, quadrants)
print(reduce(mul, quadrants, 1))