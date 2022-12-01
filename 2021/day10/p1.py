from queue import LifoQueue

with open('inp.txt') as f:
    lines = [list(s) for s in f.read().split('\n')]

brackets = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'    
}
scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

ans = 0

for line in lines:
    st = LifoQueue()
    for b in line:
        if b in brackets:
            st.put(b)
        else:
            top = st.get()
            if brackets[top] != b:
                ans += scores[b]
                break

print(ans)
