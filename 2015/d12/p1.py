import re

with open('inp.txt') as f:
    line = f.read()

ints = re.findall(r'-?\b\d+\b', line)

print(sum(map(int, ints)))
