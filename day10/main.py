from collections import deque
close_d = { ')': 0, '}': 0, ']': 0, '>' : 0 }
close_score = { ')': 1, '}': 3, ']': 2, '>' : 4 }
map_c = { '(': ')', '{': '}', '[': ']', '<': '>' }

scores = []
for l in open('input.txt'):
    l = l.strip()
    expected_close = deque()
    for c in l:
        if c in map_c.keys():
            expected_close.append(map_c[c])
        elif c in close_d.keys() and c != expected_close.pop():
            close_d[c] += 1
            break
    else:
        score = 0
        for c in reversed(list(expected_close)):
            score = score * 5 + close_score[c]

        scores.append(score)

print(close_d[')']*3 + close_d[']']*57 +
      close_d['}']*1197 + close_d['>'] * 25137)
print(sorted(scores)[len(scores) // 2])
