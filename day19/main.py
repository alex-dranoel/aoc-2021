from itertools import combinations, permutations, product

scanners = []
for l in open('input.txt'):
    l = l.strip()
    if l == '':
        continue

    if l.startswith('---'):
        scanners.append(set())
        continue

    beacon = tuple(map(int, l.split(',')))
    scanners[-1].add(beacon)

# prepare list for absolute positions of scanner
# and absolute position of beacons
scanners_pos = [None]*len(scanners)
scanners_pos[0] = (0,0,0)
abs_coord = [None]*len(scanners)
abs_coord[0] = scanners[0]

# generate the list of 24 bases 
flip_axes = [1, -1]
bases = []
for x in flip_axes:
    for y in flip_axes:
        for z in flip_axes:
            for b in permutations([[x, 0, 0], [0, y, 0], [0, 0, z]]):
                # only add right-handed systems (check by doing a cross product check)
                if (b[0][1]*b[1][2]-b[0][2]*b[1][1]) == b[2][0] and \
                   (b[0][2]*b[1][0]-b[0][0]*b[1][2]) == b[2][1] and \
                   (b[0][0]*b[1][1]-b[0][1]*b[1][0]) == b[2][2]:
                    bases.append(b)


def change_to_basis(v, b):
    return (b[0][0]*v[0] + b[0][1]*v[1] + b[0][2]*v[2], \
            b[1][0]*v[0] + b[1][1]*v[1] + b[1][2]*v[2], \
            b[2][0]*v[0] + b[2][1]*v[1] + b[2][2]*v[2])


def get_overlap(s1, s2):
    for b in bases:
        new_s2 = tuple(change_to_basis(v, b) for v in s2)

        for p1, p2 in product(s1, new_s2):
            delta = (p2[0]-p1[0], p2[1]-p1[1], p2[2]-p1[2])
            abs_s2 = set((p[0]-delta[0], p[1]-delta[1], p[2]-delta[2]) for p in new_s2)
            n_common = len(s1.intersection(abs_s2))
            if n_common >= 12:
                return abs_s2, delta

    return None, None


while not all(pos is not None for pos in scanners_pos):
    # compare each known scanner to unknown ones
    for i in range(len(scanners)):
        # can't compare with unknown position
        if scanners_pos[i] is None:
            continue

        for j in range(len(scanners)):
            # compare only to unknown scanner
            if i == j or scanners_pos[j] is not None:
                continue

            new_coord, pos = get_overlap(abs_coord[i], scanners[j])
            abs_coord[j] = new_coord
            scanners_pos[j] = pos


n_beacons = set()
for beacons in abs_coord:
    n_beacons |= beacons

print('Part 1:', len(n_beacons))

print('Part 2:', max(abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2]) for a,b in combinations(scanners_pos, 2)))
