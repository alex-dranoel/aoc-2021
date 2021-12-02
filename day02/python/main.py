import numpy as np

arr = [l.strip() for l in open('input.txt')]

x = 0
y = 0

print(arr)
for l in arr:
    l = l.split()
    print(l)
    if l[0] == 'forward':
        x += int(l[1])
    elif l[0] == 'down':
        y += int(l[1])
    elif l[0] == 'up':
        y -= int(l[1])

print('Part 1:', x*y)


arr = [l.strip() for l in open('input.txt')]

x = 0
y = 0
aim = 0

print(arr)
for l in arr:
    l = l.split()
    print(l)
    if l[0] == 'forward':
        x += int(l[1])
        y += aim * int(l[1])
    elif l[0] == 'down':
        aim += int(l[1])
    elif l[0] == 'up':
        aim -= int(l[1])

print('Part 2:', x*y)