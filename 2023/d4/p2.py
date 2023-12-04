from queue import Queue

with open("inp2.txt") as f:
    lines = f.read().split('\n')

ans = 0
d = {}
q = Queue()

for line in lines:
    cid, numbers = line.split(':')
    cid = int(cid[4:])
    winner, ours = numbers.split('|')
    ws = set(winner.split())
    os = set(ours.split())
    matches = ws & os
    d[cid] = len(matches)
    q.put(cid)


while not q.empty():
    ans += 1
    k = q.get()
    for i in range(k + 1, k + d[k] + 1):
        q.put(i)

print(ans)
