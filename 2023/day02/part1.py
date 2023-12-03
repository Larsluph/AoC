import re

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

game_id_pattern = re.compile(r'^Game (\d+):')
red_pattern = re.compile(r'(\d+) red')
green_pattern = re.compile(r'(\d+) green')
blue_pattern = re.compile(r'(\d+) blue')

def match_set(pattern, set):
    res = pattern.search(set)
    return int(res.group(1)) if res else 0

with open('input.txt', encoding='ascii') as f:
    lines = f.readlines()

game_ids = []

for line in lines:
    game_id = int(game_id_pattern.match(line).group(1))

    start_index = line.index(': ') + 2
    game_content = line[start_index:]
    sets = game_content.split('; ')

    flags = [True] * 3
    for red in map(lambda x: match_set(red_pattern, x), sets):
        if red > MAX_RED:
            flags[0] = False
            break
    for green in map(lambda x: match_set(green_pattern, x), sets):
        if green > MAX_GREEN:
            flags[1] = False
            break
    for blue in map(lambda x: match_set(blue_pattern, x), sets):
        if blue > MAX_BLUE:
            flags[2] = False
            break

    if False not in flags:
        game_ids.append(game_id)

print(sum(game_ids))
