import hashlib

with open('inp.txt') as f:
    line = f.read()

i = 1
while True:
    if hashlib.md5(f'{line}{i}'.encode()).hexdigest()[:5] == '00000':
        print(i)
        break
    i += 1
