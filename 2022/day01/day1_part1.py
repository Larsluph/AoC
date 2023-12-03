# each line = calories taken by elf
# blank line = next elf

inventory = list()

with open('input.txt', 'r') as f:
    current_count = 0
    for line in f.readlines():
        val = line.strip()
        if val == "":
            inventory.append(current_count)
            current_count = 0
        else:
            current_count += int(val)

print(max(inventory))
