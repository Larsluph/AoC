with open("day3\\input.txt", 'r') as f:
    lines = f.readlines()

masks = [
    "", # mask_oxy
    ""  # mask_co2
]

last_match = [
    None, # last_match_oxy
    None  # last_match_co2
]

for i in range(len(lines[0])-1):
    # print(f"col no {i}: ", end="")
    # print(masks, last_match)

    count = [
        [0, 0], # count_oxy
        [0, 0]  # count_co2
    ]

    for line in lines:
        for x in range(2):
            if line.startswith(masks[x]):
                # print(f"{x}: match found: {line[:-1]}")
                last_match[x] = line[:-1]
            else:
                # print(f"{x}: skipping: {line[:-1]}")
                continue

            if len(line) == len(masks[x]):
                # print(f"{x} found: {masks[x]}")
                continue

            if line[i] == "0":
                count[x][0] += 1
            else:
                count[x][1] += 1

    if sum(count[0]) == 1:
        masks[0] = last_match[0]
    if sum(count[1]) == 1:
        masks[1] = last_match[1]

    # check for oxygen rating
    if count[0][0] > count[0][1]:
        masks[0] += "0"
    else:
        masks[0] += "1"

    # check for co2 rating
    if count[1][0] > count[1][1]:
        masks[1] += "1"
    else:
        masks[1] += "0"

assert last_match[0]+"\n" in lines, "Can't find oxygen rating"
assert last_match[1]+"\n" in lines, "Can't find CO2 rating"

oxygen_gen_rating = int(last_match[0], 2)
co2_scurb_rating = int(last_match[1], 2)

print(oxygen_gen_rating, co2_scurb_rating)
print(oxygen_gen_rating * co2_scurb_rating)
