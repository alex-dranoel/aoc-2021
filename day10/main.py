from collections import deque
d = { ')': 0, '}': 0, ']': 0, '>' : 0 }

scores = []
for i, l in enumerate(open('input.txt')):
    l = l.strip()
    expected_close = deque()
    is_bad = False
    for c in l:
        if c == '(':
            expected_close.append(')')
        elif c == '{':
            expected_close.append('}')
        elif c == '[':
            expected_close.append(']')
        elif c == '<':
            expected_close.append('>')
        elif c in d.keys() and c != expected_close.pop():
            d[c] += 1
            is_bad = True
            break
    
    if not is_bad:
        score = 0
        for c in reversed(list(expected_close)):
            add = 0
            if c == ')':
                add = 1
            elif c == ']':
                add = 2
            elif c == '}':
                add = 3
            elif c == '>':
                add = 4

            score = score * 5 + add

        scores.append(score)

print(d[')']*3 + d[']']*57 + d['}']*1197 + d['>'] * 25137)
print(sorted(scores)[len(scores) // 2])
