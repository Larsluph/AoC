chunk_delimiters_open = dict(zip("([{<", range(4)))
chunk_delimiters_close = dict(zip(")]}>", range(4)))

def reverse_dict(d, value):
    for k, v in d.items():
        if v == value:
            return k
    return None

with open("day10\\input.txt", 'r') as f:
    data = f.readlines()

scores = list()

for i, line in enumerate(data, start=1):
    line = line.strip()
    stack = list()
    for j, token in enumerate(line, start=1):
        if token in chunk_delimiters_open:
            stack.append(chunk_delimiters_open[token])
        elif token in chunk_delimiters_close:
            t = stack.pop()
            if t != chunk_delimiters_close[token]:
                # corrupted
                break
    if len(stack) > 0 and j == len(line):
        # incomplete
        print(f"detected incomplete chunk in subsystem at line {i:03}: {stack}")
        score = 0
        while stack:
            s = stack.pop()
            score *= 5
            score += s+1
        scores.append(score)

scores.sort()

# print(scores)
print(scores[int(len(scores)/2)])
