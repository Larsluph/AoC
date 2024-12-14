from math import ceil
import re
from itertools import batched, product

button_pattern = re.compile(r'Button \w: X(?P<x>[+-]\d+), Y(?P<y>[+-]\d+)')
prize_pattern = re.compile(r'Prize: X=(?P<x>\d+), Y=(?P<y>\d+)')

with open('input.txt', encoding='ascii') as f:
    lines = filter(len, map(str.strip, f.readlines()))

COST_A = 3
COST_B = 1

total_tokens = 0
for button_a, button_b, prize in batched(lines, 3, strict=True):
    match_a = button_pattern.match(button_a)
    match_b = button_pattern.match(button_b)
    match_prize = prize_pattern.match(prize)

    assert match_a is not None
    assert match_b is not None
    assert match_prize is not None

    a_x, a_y = int(match_a.group('x')), int(match_a.group('y'))
    b_x, b_y = int(match_b.group('x')), int(match_b.group('y'))
    prize_x, prize_y = int(match_prize.group('x')), int(match_prize.group('y'))

    max_iter = max(ceil(prize_x / a_x), ceil(prize_x / b_x),
                   ceil(prize_y / a_y), ceil(prize_y / b_y))
    iter_limit = min(max_iter, 100)

    success = False
    min_cost = iter_limit*5
    for a, b in product(range(iter_limit), repeat=2):
        if a*a_x + b*b_x == prize_x and a*a_y + b*b_y == prize_y:
            success = True
            token_cost = a*COST_A + b*COST_B
            min_cost = min(min_cost, token_cost)

    print(success, min_cost)
    if success:
        total_tokens += min_cost

print(total_tokens)
