with open('input.txt', 'r', encoding='ascii') as f:
    raw_lines = f.readlines()

prev_beams: dict[int, int] = None
beams: dict[int, int] = {}
for i_line, raw_line in enumerate(raw_lines):
    for i_char, char in enumerate(raw_line.strip()):
        if i_line == 0:
            if char == "S":
                beams[i_char] = 1
            continue

        if char == '^' and i_char in prev_beams:
            beams[i_char-1] = prev_beams[i_char] + (beams[i_char-1] if i_char-1 in beams else 0)
            beams[i_char+1] = prev_beams[i_char] + (beams[i_char+1] if i_char+1 in beams else 0)
            continue

        if char == '.' and i_char in prev_beams:
            beams[i_char] = prev_beams[i_char] + (beams[i_char] if i_char in beams else 0)
            continue

    #print(beams)
    prev_beams = beams
    beams = {}

print(sum(prev_beams.values()))
