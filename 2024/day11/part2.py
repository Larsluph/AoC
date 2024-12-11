from functools import cache

with open('input.txt', encoding='ascii') as f:
    stones = list(map(int, f.read().split()))

@cache
def get_next_stones(stone: int, steps: int):
    if steps == 0:
        return 1

    if stone == 0:
        return get_next_stones(1, steps - 1)

    stone_str = str(stone)
    if (length := len(stone_str)) % 2 == 0:
        half = length // 2
        return (get_next_stones(int(stone_str[:half]), steps - 1) +
                get_next_stones(int(stone_str[half:]), steps - 1))

    return get_next_stones(stone * 2024, steps - 1)

print(sum(get_next_stones(s, 75) for s in stones))
