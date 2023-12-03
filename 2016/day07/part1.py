def get_brackets_bounds(input: str):
    num_occurs = input.count('[')
    last_index = 0
    for i in range(num_occurs):
        o_i = input.find('[', last_index)
        c_i = input.find(']', last_index)
        yield (o_i, c_i)
        last_index = c_i + 1

def inside_text(input: str):
    bounds = get_brackets_bounds(input)
    final = []
    for o,c in bounds:
        final.append(input[o+1:c])
    return " ".join(final)

def outside_text(input: str):
    bounds = get_brackets_bounds(input)
    last_index = 0
    final = []
    for o,c in bounds:
        final.append(input[last_index:o])
        last_index = c+1
    else:
        final.append(input[last_index:])
    return " ".join(final)

def detect_tls(raw: str):
    data_in = inside_text(raw)
    data_out = outside_text(raw)

    detected_in = False
    detected_out = False


    # Detect in abba
    for i_start in range(len(data_in)-3):
        a,b,c,d = tuple(data_in[i_start:i_start+4])
        detected_in = detected_in or (a == d) and (b == c) and (a != b)

    # Detect out abba
    for i_start in range(len(data_out)-3):
        a,b,c,d = tuple(data_out[i_start:i_start+4])
        detected_out = detected_out or (a == d) and (b == c) and (a != b)

    return detected_out and not detected_in

total_count = 0
with open('day07\\input.txt') as f:
    for line in f.readlines():
        total_count += int(detect_tls(line.strip()))
print(total_count)
