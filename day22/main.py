import re

def range_intersect(r1, r2):
    return range(max(r1.start, r2.start), min(r1.stop, r2.stop)) or None
        
class Range3D:

    def __init__(self, ranges):
        self.x = ranges[0]
        self.y = ranges[1]
        self.z = ranges[2]

    def volume(self):
        return (self.x[-1]+1-self.x[0])*(self.y[-1]+1-self.y[0])*(self.z[-1]+1-self.z[0])

    def find_intersect(self, other):
        cx = range_intersect(self.x, other.x)
        cy = range_intersect(self.y, other.y)
        cz = range_intersect(self.z, other.z)
        return cx, cy, cz

    def keep_non_overlap(self, other):
        cx, cy, cz = self.find_intersect(other)

        # in case there is no overlap, return self
        if not cx or not cy or not cz:
            return [self]
        
        # in case self range is completely found in other range, in other words, self is contained in other
        if cx == self.x and cy == self.y and cz == self.z:
            return []

        # Now other is either completely or partly inside self. In either case, only the part that is inside
        # should be considered, that is only the intersection should be considered

        # Now we will compute the set of volumes that are left after the exclusion of the common part

        remaining_cubes = []
        left_x = range(self.x[0], cx[0])
        left_y = range(self.y[0], self.y[-1]+1)
        left_z = range(self.z[0], self.z[-1]+1)
        if left_x:
            remaining_cubes.append(Range3D([left_x, left_y, left_z]))

        right_x = range(cx[-1]+1, self.x[-1]+1)
        right_y = range(self.y[0], self.y[-1]+1)
        right_z = range(self.z[0], self.z[-1]+1)
        if right_x:
            remaining_cubes.append(Range3D([right_x, right_y, right_z]))
        
        front_x = range(cx[0] if left_x else self.x[0], (cx[-1]+1) if right_x else (self.x[-1]+1))
        front_y = range(self.y[0], cy[0])
        front_z = range(self.z[0], self.z[-1]+1)
        if front_y:
            remaining_cubes.append(Range3D([front_x, front_y, front_z]))

        back_x = range(cx[0] if left_x else self.x[0], (cx[-1]+1) if right_x else (self.x[-1]+1))
        back_y = range(cy[-1]+1, self.y[-1]+1)
        back_z = range(self.z[0], self.z[-1]+1)
        if back_y:
            remaining_cubes.append(Range3D([back_x, back_y, back_z]))

        bottom_x = range(cx[0] if left_x else self.x[0], (cx[-1]+1) if right_x else (self.x[-1]+1))
        bottom_y = range(cy[0] if front_y else self.y[0], (cy[-1]+1) if back_y else (self.y[-1]+1))
        bottom_z = range(self.z[0], cz[0])
        if bottom_z:
            remaining_cubes.append(Range3D([bottom_x, bottom_y, bottom_z]))

        top_x = range(cx[0] if left_x else self.x[0], (cx[-1]+1) if right_x else (self.x[-1]+1))
        top_y = range(cy[0] if front_y else self.y[0], (cy[-1]+1) if back_y else (self.y[-1]+1))
        top_z = range(cz[-1]+1, self.z[-1]+1)
        if top_z:
            remaining_cubes.append(Range3D([top_x, top_y, top_z]))

        
        return remaining_cubes

## some tests        
# c1 = Range3D([range(0,10),range(0,10),range(0,10)])
# c2 = Range3D([range(0,11),range(0,10),range(0,10)])
# l = c1.keep_non_overlap(c2)
# print(l)
# print(c1.volume())


on_cubes = []
for l in open('input.txt'):
    l = l.strip()
    action = 1 if l.startswith('on') else 0
    (x_low, x_high, y_low, y_high, z_low, z_high) = list(
        map(int, re.findall('(-?\d+)', l)))

    if x_high < -50 or x_low > 50:
        continue
    if y_high < -50 or y_low > 50:
        continue
    if z_high < -50 or z_low > 50:
        continue

    x = range(x_low, x_high+1)
    y = range(y_low, y_high+1)
    z = range(z_low, z_high+1)
    cub = Range3D([x, y, z])
    new_on_cubes = []
    for on_cube in on_cubes:
        new_on_cubes.extend(on_cube.keep_non_overlap(cub))
    
    if action == 1:
        new_on_cubes.append(cub)

    on_cubes = new_on_cubes

print(sum(c.volume() for c in on_cubes))