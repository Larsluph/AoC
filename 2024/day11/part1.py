with open('input.txt', encoding='ascii') as f:
    old_data = list(map(int, f.read().split()))

for i in range(25):
    new_data = []
    for stone in old_data:
        stone_str = str(stone)
        if stone == 0:
            new_data.append(1)
        elif (length := len(stone_str)) % 2 == 0:
            half = length // 2
            new_data.append(int(stone_str[:half]))
            new_data.append(int(stone_str[half:]))
        else:
            new_data.append(stone * 2024)
    old_data = new_data
    # print(old_data)
    # print('================')

print(len(old_data))
