def check_different(flag: str):
    return len(set(flag)) == len(flag)

with open('input.txt', 'r') as f:
    ptr = 13
    buffer = '\0' + f.read(13)
    while (data := f.read(1)) != '':
        ptr += 1
        buffer = buffer[1:] + data
        if check_different(buffer):
            print(f'marker: {buffer} {ptr}')
            break
