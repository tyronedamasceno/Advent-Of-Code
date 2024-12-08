with open('inp.txt') as f:
    line = f.read()

print(line.count('(') - line.count(')'))
