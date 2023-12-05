from collections import defaultdict

from tqdm import tqdm

with open("inp.txt") as f:
    lines = f.read().split('\n')
    lines = [line for line in lines if line]

d = defaultdict(dict)

seeds = [int(k) for k in lines[0][7:].split()]
seeds2 = sorted([
    (seeds[i], seeds[i + 1])
    for i in range(0, len(seeds), 2)
])

for line in lines[1:]:
    if 'map' in line:
        src, _, dst = line[:-5].split('-')
        continue

    dst_base, src_base, length = [int(k) for k in line.split()]
    d[src][src_base] = (dst_base, length)

mappings = {
    r: sorted(d[r].items())
    for r in d.keys()
}


def _get_mapping(value, resource):
    for src, (dst, l) in mappings[resource]:
        if value >= src and value < src + l:
            return dst + value - src
    return value


ans = float('inf')
for base_seed, length in seeds2:
    print(length)
    for seed in tqdm(range(base_seed, base_seed + length)):
        soil = _get_mapping(seed, 'seed')
        fertilizer = _get_mapping(soil, 'soil')
        water = _get_mapping(fertilizer, 'fertilizer')
        light = _get_mapping(water, 'water')
        temperature = _get_mapping(light, 'light')
        humidity = _get_mapping(temperature, 'temperature')
        location = _get_mapping(humidity, 'humidity')
        ans = min(ans, location)

print(ans)
