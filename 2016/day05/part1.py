from hashlib import md5

with open('day05\\input.txt') as f:
    door_id = f.read()

index = 0
final_password = ''
while len(final_password) < 8:
    pwd = f'{door_id}{index}'.encode()
    h = md5(pwd).hexdigest()
    if h[:5] == '00000':
        final_password += h[5]
        print(f'found matching hash with index {index}')
    index += 1

print(final_password)
