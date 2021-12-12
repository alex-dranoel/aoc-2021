from collections import defaultdict
from copy import copy

connections = defaultdict(list)
for l in open('input.txt'):
    src, dest = l.strip().split('-')
    connections[src].append(dest)
    connections[dest].append(src)

# first part, with a set for visited nodes
def count_paths(src, dest, visited):

    # reached the destination -> count as valid path
    if src == dest:
        return 1

    # reached a lower case already visited -> abort path
    if src.islower() and src in visited:
        return 0
   
    # continue search
    # adds current node to visited list of current search
    new_visited = visited.union({src})

    # sum up all paths that reach destination from any adjacent points
    return sum(count_paths(adj, dest, new_visited) for adj in connections[src])


visited = set()
print('Part 1:', count_paths('start', 'end', visited))

# first and second part, with a dictionary for visited nodes
def count_paths(src, dest, visited, allowed_visit):

    # reached the destination -> count as valid path
    if src == dest:
        return 1

    # reached a lower case already visited -> abort path
    if src.islower() and src in visited.keys():
        if src == 'start' or visited[src] >= allowed_visit:
            return 0
        else:
            allowed_visit = 1
    
    # continue search
    # adds current node to visited list of current search
    new_visited = copy(visited)
    new_visited[src] += 1

    # sum up all paths that reach destination from any adjacent points
    return sum(count_paths(adj, dest, new_visited, allowed_visit) for adj in connections[src])

print('Part 1:', count_paths('start', 'end', defaultdict(int), 1))
print('Part 2:', count_paths('start', 'end', defaultdict(int), 2))

