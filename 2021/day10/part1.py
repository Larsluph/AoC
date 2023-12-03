table = [3, 57, 1197, 25137]

chunk_delimiters_open = dict(zip("([{<", range(4)))
chunk_delimiters_close = dict(zip(")]}>", range(4)))

def reverse_dict(d, value):
    for k, v in d.items():
        if v == value:
            return k
    return None

with open("day10\\input.txt", 'r') as f:
    data = f.readlines()

syntax_err_score = 0

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
                print(f"detected corrupted chunk at line {i:03} (col {j:03}): expected '{reverse_dict(chunk_delimiters_close, t)}' got '{token}'")
                syntax_err_score += table[chunk_delimiters_close[token]]
                break

print(syntax_err_score)
