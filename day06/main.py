from collections import Counter

d = {str(i): 0 for i in range(9)}
d.update(Counter(open('input.txt').readline()))

for _ in range(256):
    new_d = {str(i):0 for i in range(9)}
    new_d['6'] += d['0']
    new_d['8'] += d['0']
    for j in range(8):
        new_d[str(j)] += d[str(j+1)]

    d = new_d

print(sum(d.values()))

