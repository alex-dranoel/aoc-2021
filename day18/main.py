import re
from itertools import permutations


def left_most_5nested_pair(n):
    count_open_brack = 0
    left_most_pair_start_idx = None
    left_most_pair_end_idx = None
    for i, c in enumerate(n):
        if c == '[':
            if count_open_brack == 4:
                left_most_pair_start_idx = i

            count_open_brack += 1

        elif c == ']':
            if left_most_pair_start_idx:
                left_most_pair_end_idx = i

            count_open_brack -= 1

        if left_most_pair_start_idx and left_most_pair_end_idx:
            return (left_most_pair_start_idx, left_most_pair_end_idx)

    return None


def split_left_most_big_nbr(n):
    m = re.search(r'(\d{2,})', n)
    if m:
        idx = m.start(1)
        to_replace = m.groups(1)[0]
        left_nbr = str(int(to_replace)//2)
        right_nbr = str((int(to_replace)+1)//2)
        n = n[:idx] + '[' + left_nbr + ',' + right_nbr + ']' + n[idx+len(to_replace):]
    
    return n


def reduce(n):
    while True:
        prev_n = n
        pair_idx = left_most_5nested_pair(n)
        if pair_idx:
            pair = n[pair_idx[0]:pair_idx[1]+1]
            pl, pr = pair[1:-1].split(',')
            left = n[:pair_idx[0]]
            right = n[pair_idx[1]+1:]

            m = re.search(r'(\d+)', left[::-1])
            if m:
                idx = len(left)-m.end(1)
                to_replace = m.groups(1)[0][::-1]
                left = left[:idx] + str(int(to_replace) + int(pl)) + left[idx+len(to_replace):]
            m = re.search(r'(\d+)', right)
            if m:
                idx = m.start(1)
                to_replace = m.groups(1)[0]
                right = right[:idx] + str(int(to_replace) + int(pr)) + right[idx+len(to_replace):]
            
            n = left + '0' + right
            continue
        
        n = split_left_most_big_nbr(n)
        if prev_n == n:
            break
    
    return n


def magnitude(pair):
    if pair[1].isdigit() and pair[-2].isdigit():
        return 3*int(pair[1]) + 2*int(pair[-2])
    if pair[1].isdigit() and not pair[-2].isdigit():
        return 3*int(pair[1]) + 2*magnitude(pair[3:-1])
    if not pair[1].isdigit() and pair[-2].isdigit():
        return 3*magnitude(pair[1:-3]) + 2*int(pair[-2])
    else:
        open_bracket = 1
        split = None
        for i,c in enumerate(pair[2:-1]):
            if c == '[':
                open_bracket += 1
            if c == ']':
                open_bracket -= 1
            if open_bracket == 0:
                split = 2+i+1
                break
            
        return 3*magnitude(pair[1:split]) + 2*magnitude(pair[split+1:-1])


def add(n1, n2):
    n = '[' + n1 + ',' + n2 + ']'
    return reduce(n)


nbrs = [l.strip() for l in open('input.txt')]
red_sum = nbrs[0]
for n in nbrs[1:]:
    red_sum = add(red_sum, n)

print('Part 1:', magnitude(red_sum))

max_mag = 0
for combination in permutations(nbrs, 2):
    red_sum = add(combination[0], combination[1])
    red_sum = reduce(red_sum)
    mag = magnitude(red_sum)
    max_mag = max(max_mag, mag)

print('Part 2:', max_mag)