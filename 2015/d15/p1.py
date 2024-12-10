with open('inp.txt') as f:
    lines = f.read().splitlines()

ings = []
cap = {}
dur = {}
fla = {}
tex = {}
# cal = {}

for line in lines:
    ing, props = line.split(': ')
    ings.append(ing)
    props = props.split(', ')
    props = [int(p.split()[1]) for p in props]
    cap[ing] = props[0]
    dur[ing] = props[1]
    fla[ing] = props[2]
    tex[ing] = props[3]
    # cal[ing] = props[4]

ans = -1
for i in range(1, 101):
    for j in range(1, 101 - i):
        for k in range(1, 101 - i - j):
            h = 100 - i - j - k

            caps = max(0, i * cap[ings[0]] + j * cap[ings[1]] + k * cap[ings[2]] + h * cap[ings[3]])
            durs = max(0, i * dur[ings[0]] + j * dur[ings[1]] + k * dur[ings[2]] + h * dur[ings[3]])
            flas = max(0, i * fla[ings[0]] + j * fla[ings[1]] + k * fla[ings[2]] + h * fla[ings[3]])
            texs = max(0, i * tex[ings[0]] + j * tex[ings[1]] + k * tex[ings[2]] + h * tex[ings[3]])

            ans = max(ans, caps * durs * flas * texs)


print(ans)
