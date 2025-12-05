from intervaltree import IntervalTree

with open('input.txt', 'r', encoding='ascii') as f:
    raw_lines = f.readlines()

tree = IntervalTree()
available_ids = []

parse_step = 1
for raw_line in raw_lines:
    if raw_line == "\n":
        parse_step += 1
        continue

    match parse_step:
        case 1:
            start, end = list(map(int, raw_line.strip().split("-")))
            tree.addi(start, end+1)
        case 2:
            available_ids.append(int(raw_line.strip()))

tree.merge_overlaps()
id_count = 0
for interval in tree.items():
    id_count += interval.end - interval.begin
print(id_count)
