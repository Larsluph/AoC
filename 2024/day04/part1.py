with open('input.txt', encoding='ascii') as f:
    matrix = list(map(lambda x: list(x.strip()), f.readlines()))

mat_size = len(matrix)

def safe_matrix(a, b):
    if 0 <= a < mat_size and 0 <= b < mat_size:
        return matrix[b][a]
    return None

directions = [
    (0, -1),  # left
    (0, 1),   # right
    (-1, 0),  # up
    (1, 0),   # down
    (-1, -1), # diagonal up-left
    (-1, 1),  # diagonal up-right
    (1, -1),  # diagonal bottom-left
    (1, 1)    # diagonal bottom-right
]

pattern = 'XMAS'

total = 0
for y in range(mat_size):
    for x in range(mat_size):
        for dy, dx in directions:
            iter = tuple((k, x + k * dx, y + k * dy) for k in range(len(pattern)))
            if all(map(lambda aa: safe_matrix(aa[1], aa[2]) == pattern[aa[0]], iter)):
                print(iter)
                print(*map(lambda aa: safe_matrix(aa[1], aa[2]), iter))
                print(f'match found : {x=}, {y=}, {dx=}, {dy=}')
                total += 1

print(total)

print(matrix[0][4], matrix[1][5], matrix[2][6], matrix[3][7])
print(matrix[0][5], matrix[0][6], matrix[0][7], matrix[0][8])
