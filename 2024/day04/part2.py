with open('input.txt', encoding='ascii') as f:
    matrix = list(map(lambda x: list(x.strip()), f.readlines()))

mat_size = len(matrix)


def safe_matrix(a, b):
    if 0 <= a < mat_size and 0 <= b < mat_size:
        return matrix[b][a]
    return None


patterns = [
    #M M
    # A
    #S S
    {
        'M': [
            (0, 0),
            (2, 0),
        ],
        'A': [
            (1, 1),
        ],
        'S': [
            (0, 2),
            (2, 2),
        ]
    },
    #M S
    # A
    #M S
    {
        'M': [
            (0, 0),
            (0, 2),
        ],
        'A': [
            (1, 1),
        ],
        'S': [
            (2, 0),
            (2, 2),
        ]
    },
    #S S
    # A
    #M M
    {
        'M': [
            (0, 2),
            (2, 2),
        ],
        'A': [
            (1, 1),
        ],
        'S': [
            (0, 0),
            (2, 0),
        ]
    },
    #S M
    # A
    #S M
    {
        'M': [
            (2, 0),
            (2, 2),
        ],
        'A': [
            (1, 1),
        ],
        'S': [
            (0, 0),
            (0, 2),
        ]
    }
]

def check_pattern(pat: dict, a: int, b: int):
    for k, v in pat.items():
        for x_pos, y_pos in v:
            if safe_matrix(a+x_pos, b+y_pos) != k:
                return False
    return True

total = 0
for y in range(mat_size):
    for x in range(mat_size):
        for pattern in patterns:
            total += int(check_pattern(pattern, x, y))

print(total)
