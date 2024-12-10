import json

with open('inp.txt') as f:
    line = f.read()


def check_reds(dt):
    if isinstance(dt, int):
        return dt

    if isinstance(dt, list):
        return sum(check_reds(k) for k in dt)

    if isinstance(dt, dict):
        if 'red' in dt.values():
            return 0
        tmp = 0
        for v in dt.values():
            tmp += check_reds(v)
        return tmp

    return 0


print(check_reds(json.loads(line)))
