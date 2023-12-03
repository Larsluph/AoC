from collections import Counter

with open("day8\\input.txt", 'r') as f:
    data = list(map(lambda x: x.strip().split(" | "), f.readlines()))
    data = list(map(lambda x: list(map(lambda x: x.split(" "), x)), data))

def reverse_dict(d, value):
    res = list()
    for k, v in d.items():
        if v == value:
            res.append(k)
    return res

def get_common(patterns):
    common = list(patterns[0])
    for pattern in patterns[1:]:
        for letter in common:
            if letter not in pattern:
                common.remove(letter)
    return common

def get_intersect(a: str, b: str):
    if len(a) < len(b):
        a, b = b, a

    for char_a in a:
        if char_a not in b:
            return char_a

def get_0(patterns: list[str], pattern_1) -> str:
    segs = Counter()
    for pattern in patterns:
        segs += Counter(pattern)
    vals = reverse_dict(segs, 5)
    vals.remove(get_common((vals, pattern_1))[0])
    for pattern in patterns:
        if vals[0] not in pattern:
            return pattern

def get_3(patterns):
    temp = Counter()
    for pattern in patterns:
        temp += Counter(pattern)
    
    _filter = list()
    for letter, count in temp.items():
        if count == 2:
            _filter.append(letter)
    
    for pattern in patterns:
        if all([f in pattern for f in _filter]):
            return pattern

def get_25(patterns):
    patterns_5 = list()
    patterns_6 = list()
    for pattern in patterns:
        (patterns_5 if len(pattern) == 5 else patterns_6).append(pattern)

    for letter in patterns_5[0]:
        for pattern in patterns_6:
            if letter not in pattern:
                return patterns_5
    return patterns_5[::-1]
"""
[
    [10 signal patterns, 4 digit value],
    ...
]

obvious:
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

d = {2: 1, 3: 7, 4: 4, 7: 8}
result = 0

for patterns, output in data:
    patterns = list(map(lambda x: "".join(sorted(x)), patterns))
    output = list(map(lambda x: "".join(sorted(x)), output))
    # print(patterns, output, sep="\n")
    segments = dict()

    # obvious patterns
    for pattern in patterns.copy():
        l = len(pattern)
        if l in d:
            segments[pattern] = d[l]
            patterns.remove(pattern)

    p1 = reverse_dict(segments, 1)[0]

    p0 = get_0(patterns, p1)
    segments[p0] = 0
    patterns.remove(p0)

    p3 = get_3([pattern for pattern in patterns if len(pattern) == 5])
    segments[p3] = 3
    patterns.remove(p3)

    p2, p5 = get_25(patterns)
    segments[p2] = 2
    patterns.remove(p2)
    segments[p5] = 5
    patterns.remove(p5)

    if p1[0] in patterns[0] and p1[1] in patterns[0]:
        p9, p6 = patterns
    else:
        p6, p9 = patterns
    segments[p6] = 6
    patterns.remove(p6)
    segments[p9] = 9
    patterns.remove(p9)

    temp_res = ""
    for pat in output:
        pat = "".join(sorted(pat))
        try:
            temp_res += str(segments[pat])
        except:
            temp_res += "/"
    # print(temp_res)
    result += int(temp_res)

# print(segments)
# print(patterns)
print(result)
