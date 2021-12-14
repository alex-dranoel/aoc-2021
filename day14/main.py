from collections import defaultdict
from collections import Counter
from copy import copy

temp = open('input.txt').readline().strip()
d = { k: v for k, v in [ l.strip().split(' -> ') for l in open('input.txt').readlines()[2:] ] }

for _ in range(10):
    temp = ''.join(c + d.get(temp[j:(j+2)], '') for j,c in enumerate(temp))

c = Counter(temp)
print('Part 1:', c.most_common()[0][1] - c.most_common()[-1][1])

temp = open('input.txt').readline().strip()
pair_counter = defaultdict(int)
for i in range(len(temp)-1):
    pair_counter[temp[i:i+2]] += 1

for _ in range(40):
    new_pair_counter = copy(pair_counter)
    for p, v in pair_counter.items():
        if p in d.keys():
            new_pair_counter[p] -= v
            new_pair_counter[p[0] + d[p]] += v
            new_pair_counter[d[p] + p[1]] += v

    pair_counter = new_pair_counter

char_counter = defaultdict(int)
# the first and last characters of the template
# are the only one to not be double counted.
# So we had 1 so that we can divide by 2 later on.
char_counter[temp[0]] += 1
char_counter[temp[-1]] += 1
for k, v in pair_counter.items():
    char_counter[k[0]] += v
    char_counter[k[1]] += v

s = sorted(char_counter.items(), key=lambda kv: kv[1])
print('Part 2:', (s[-1][1] - s[0][1])//2)
