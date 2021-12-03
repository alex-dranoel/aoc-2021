

arr = [l.strip() for l in open('input.txt')]

n = len(arr[0])

count0 = [0] * n
for i in range(n):
    
    for l in arr:
        if l[i] == '0':
            count0[i] += 1

oneMost = ['1'] * n
zeroMost = ['0'] * n
for i in range(n):
    if count0[i] > len(arr)//2:
        oneMost[i] = '0'
        zeroMost[i] = '1'

print('Part 1:', int(''.join(oneMost), 2) * int(''.join(zeroMost), 2))

def get_most_common(pos, arr):
    count0 = 0
    for l in arr:
        if l[pos] == '0':
            count0 += 1
    
    if count0 > len(arr) // 2:
        return '0'
    elif count0 < len(arr) // 2:
        return '1'
    else:
        return '-1'

import copy
def get_ox(arr):
    n = len(arr[0])
    t = copy.copy(arr)
    for i in range(n):
        most_common = get_most_common(i, t)
        if most_common == '-1':
            most_common = '1'
        
        new_t = []
        for l in t:
            if l[i] == most_common:
                new_t.append(l)
        
        t = copy.copy(new_t)
        
        if len(t) == 1:
            break
    
    return t

ox = get_ox(arr)


def get_co(arr):
    n = len(arr[0])
    t = copy.copy(arr)
    for i in range(n):
        most_common = get_most_common(i, t)

        # flip the most common value because we want
        # less common for co2 rate
        if most_common == '0':
            most_common = '1'
        elif most_common == '1':
            most_common = '0'
        elif most_common == '-1':
            most_common = '0'

        new_t = []
        for l in t:
            if l[i] == most_common:
                new_t.append(l)

        t = copy.copy(new_t)

        if len(t) == 1:
            break

    return t


co = get_co(arr)

print('Part 2:', int(''.join(ox), 2) * int(''.join(co), 2))
