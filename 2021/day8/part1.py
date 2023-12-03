with open("day8\\input.txt", 'r') as f:
    data = list(map(lambda x: x.strip().split(" | "), f.readlines()))
    data = list(map(lambda x: list(map(lambda x: x.split(" "), x)), data))

"""
[
    [10 signal patterns, 4 digit value],
    ...
]

1:     c     f  : 2
7: a   c     f  : 3
4:   b c d   f  : 4
8: a b c d e f g: 7

2: a   c d e   g: 5
3: a   c d   f g: 5
5: a b   d   f g: 5

0: a b c   e f g: 6
6: a b   d e f g: 6
9: a b c d   f g: 6
"""

result = 0

for pattern, output in data:
    for x in output:
        if len(x) in (2, 3, 4, 7):
            result += 1

print(result)
