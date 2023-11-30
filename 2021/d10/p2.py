from queue import LifoQueue

with open("inp.txt") as f:
    lines = [list(s) for s in f.read().split("\n")]

brackets = {"(": ")", "[": "]", "{": "}", "<": ">"}
scores = {")": 1, "]": 2, "}": 3, ">": 4}

totals = []
for line in lines:
    st = LifoQueue()
    corrupted = False
    for b in line:
        if b in brackets:
            st.put(b)
        else:
            top = st.get()
            if brackets[top] != b:
                corrupted = True
                break
    if not st.empty() and not corrupted:
        ans = 0
        while not st.empty():
            top = st.get()
            if top not in brackets:
                continue
            ans *= 5
            ans += scores[brackets[top]]
        totals.append(ans)

print(sorted(totals)[len(totals) // 2])
