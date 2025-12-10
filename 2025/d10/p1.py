from queue import Queue

with open("inp.txt") as f:
    machines = f.read().splitlines()

lights = []
btns = []
jolts = []
for machine in machines:
    lights.append([l == "#" for l in machine[1 : machine.find("]")]])
    btns.append(
        [
            list(map(int, b[1:-1].split(",")))
            for b in machine[machine.find("]") + 1 : machine.find("{")].split()
        ]
    )
    # jolts.append(machine[machine.find("{") + 1 : -1])

ans = 0
for i, (light, btn) in enumerate(zip(lights, btns)):
    q = Queue()
    cur = [False] * len(light)

    q.put((cur[:], 0))

    seen = set()

    while not q.empty():
        cur, k = q.get()
        if tuple(cur) in seen:
            continue
        seen.add(tuple(cur))

        if cur == light:
            ans += k
            break
        for bt in btn:
            nxt = cur[:]
            for b in bt:
                nxt[b] = not nxt[b]
            q.put((nxt[:], k + 1))

print(ans)
