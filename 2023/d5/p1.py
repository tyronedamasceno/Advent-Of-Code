from collections import defaultdict

with open("inp.txt") as f:
    lines = f.read().split('\n')
    lines = [line for line in lines if line]

d = defaultdict(dict)

seeds = [int(k) for k in lines[0][7:].split()]
for line in lines[1:]:
    if 'map' in line:
        src, _, dst = line[:-5].split('-')
        continue

    dst_base, src_base, lenght = [int(k) for k in line.split()]
    for i in range(lenght):
        d[src][src_base + i] = dst_base + i

ans = float('inf')
for seed in seeds:
    soil = d['seed'].get(seed, seed)
    ferti = d['soil'].get(soil, soil)
    water = d['fertilizer'].get(ferti, ferti)
    light = d['water'].get(water, water)
    temp = d['light'].get(light, light)
    humi = d['temperature'].get(temp, temp)
    loc = d['humidity'].get(humi, humi)
    ans = min(ans, loc)

print(ans)
