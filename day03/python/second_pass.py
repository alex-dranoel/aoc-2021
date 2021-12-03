import numpy as np
from collections import Counter


arr = np.array([list(l.strip()) for l in open('input.txt')])

# part 1 -------------------
counts = np.apply_along_axis(Counter, 0, arr)
most_common = [c.most_common(1)[0][0] for c in counts]
least_common = [c.most_common()[-1][0] for c in counts]
print('Part 1:', int(''.join(most_common), 2) * int(''.join(least_common), 2))


# part 2 -------------------
def get_elem(arr, key):
    n = len(arr[0])
    t = arr
    for i in range(n):
        counter = Counter(t[:, i])
        if counter['0'] == counter['1']:
            most_common = str(key)
        else:
            most_common = counter.most_common()[1-key][0]

        t = t[t[:, i] == most_common]
        if len(t) == 1:
            break

    return t[0]

o2 = get_elem(arr, 1)
co2 = get_elem(arr, 0)

print('Part 2:', int(''.join(o2), 2) * int(''.join(co2), 2))

