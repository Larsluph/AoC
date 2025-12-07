with open('input.txt', 'r', encoding='ascii') as f:
    raw_lines = f.readlines()

split_count = 0
prev_beams: set[int] = None
beams: set[int] = set()
for i_line, raw_line in enumerate(raw_lines):
    for i_char, char in enumerate(raw_line.strip()):
        if i_line == 0:
            if char == "S":
                beams.add(i_char)
            continue

        if char == '^' and i_char in prev_beams:
            split_count += 1
            beams.update((i_char-1, i_char+1))
            continue

        if char == '.' and i_char in prev_beams:
            beams.add(i_char)
            continue

    prev_beams = beams
    beams = set()

print(split_count)
