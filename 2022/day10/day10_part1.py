reg_x = 1
reg_x_backup: int

with open('input.txt', 'r') as f:
    lines = f.readlines()

total_strength = 0
cycles_to_monitor = iter(range(20, 221, 40))
next_cycle_to_monitor = next(cycles_to_monitor)
current_cycle = 1
for line in lines:
    if current_cycle >= next_cycle_to_monitor:
        cycle_operand = reg_x_backup if current_cycle > next_cycle_to_monitor else reg_x
        signal_strength = cycle_operand * next_cycle_to_monitor
        total_strength += signal_strength
        try:
            next_cycle_to_monitor = next(cycles_to_monitor)
        except StopIteration:
            print(line, current_cycle, cycle_operand, signal_strength)
            break
        else:
            print(line, current_cycle, cycle_operand, signal_strength, "next cycle:", next_cycle_to_monitor)

    op, *args = line.strip().split(' ')
    if op.startswith("noop"):
        # nop => 1 cycle
        current_cycle += 1
    elif op.startswith("add"):
        # add => 2 cycles
        register = op[3:]
        value = int(args[0])
        current_cycle += 2
        reg_x_backup = reg_x
        reg_x += value
    else:
        # Unknown instruction
        print(f"Unknown instruction: <{op}> with args: ", args)

print(total_strength)
