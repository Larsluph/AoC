from hashlib import md5

with open('day05\\input.txt') as f:
    door_id = f.read()

index = 0
final_password = [None]*8
while any(p is None for p in final_password):
    pwd = f'{door_id}{index}'.encode()
    h = md5(pwd).hexdigest()
    if h[:5] == '00000':
        print(f'found matching hash with index {index}')
        try:
            pos = int(h[5], 16)
        except ValueError:
            print(f'Invalid pos: {pos}')
        else:
            if 0 <= pos < 8 and final_password[pos] is None:
                final_password[pos] = h[6]
                print(*('_' if p is None else p for p in final_password), sep='')
            elif pos > 7:
                print(f'Skipping invalid value {h[5]}')
            else:
                print(f'Skipping as slot {pos} is already taken...')
    index += 1

print(final_password)
