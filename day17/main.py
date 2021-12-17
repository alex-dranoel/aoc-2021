# target = [(20, 30), (-10, -5)]
target = [(206, 250), (-105, -57)]

def find_min_vx(low_x, high_x):
    v_x = 0
    while True:
        v_x += 1
        reach_x = (v_x * (v_x + 1)) // 2
        if reach_x >= low_x and reach_x <= high_x:
            return v_x


min_vx = find_min_vx(target[0][0], target[0][1])
max_vx = target[0][1]
min_vy = target[1][0]
max_vy = -target[1][0]

def is_y_speed_ok(v_y, low_y, high_y):
    speed_at_y_0 = -1*v_y - 1
    v = speed_at_y_0
    next_y = 0
    while next_y > high_y:
        next_y += v
        v -= 1

    return next_y >= low_y


print('Part 1:', (-target[1][0]-1) * (-target[1][0]) // 2)

def get_x(vx, n):
    xs_in_target = []
    x = 0
    while x <= target[0][1] and len(xs_in_target) < n:
        xs_in_target.append(x >= target[0][0])
        x += vx
        # drag
        vx -= int(vx>0)
    
    return xs_in_target

def get_y(vy):
    ys_in_target = []
    y = 0
    while y >= target[1][0]:
        ys_in_target.append(y <= target[1][1])
        # gravity
        y += vy
        vy -= 1
    
    return ys_in_target

count = 0
for vx in range(min_vx, max_vx+1):
    for vy in range(min_vy, max_vy):
        ys = get_y(vy)
        xs = get_x(vx, len(ys))
        n = min(len(ys), len(xs))
        count += int(any(x & y for x in xs[:n] for  y in ys[:n]))

print('Part 2:', count)
