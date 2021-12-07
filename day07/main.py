l = [int(c) for c in '16, 1, 2, 0, 4, 2, 7, 1, 2, 14'.split(', ')]

# these two lines solve part 1 and part 2 respectively
print(min(sum(abs(i-c) for c in l) for i in range(max(l))))
print(min(sum(abs(i-c)*(abs(i-c)+1) // 2 for c in l) for i in range(max(l))))

# without list comprehension, you need to keep track of the min yourself
# and you need to accumulate
min_fuel1 = min_fuel2 = 10000000000000
for i in range(max(l)):
    fuel1 = fuel2 = 0
    for c in l:
        steps = abs(i - c)
        fuel1 += steps
        fuel2 += steps * (steps + 1) // 2

    min_fuel1 = min(min_fuel1, fuel1)
    min_fuel2 = min(min_fuel2, fuel2)

print(min_fuel1)
print(min_fuel2)
