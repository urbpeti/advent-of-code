from collections import defaultdict, deque

def read_lines(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]

def getAllPaths(start, end, cave):
    paths = []
    q = deque()
    q.append((start, [start], set()))
    while q:
        node, path, visited = q.popleft()
        if node == end:
            paths.append(path)
            continue
        if node in visited and node.islower():
            continue

        for child in cave[node]:
            v2 = visited.copy()
            v2.add(node)
            q.append((child, path + [child], v2))

    return paths

def getAllPathPart2(start, end, cave):
    paths = []
    q = deque()
    q.append((start, [start], set(), False))
    while q:
        node, path, visited, has_small = q.popleft()
        if node == end:
            paths.append(path)
            continue
        if  node in ['start', 'end'] and len(visited) > 1:
            continue
        if node in visited and node.islower() and has_small:
            continue
        if node in visited and node.islower() and not has_small:
            has_small = True

        for child in cave[node]:
            v2 = visited.copy()
            v2.add(node)
            q.append((child, path + [child], v2, has_small))

    return paths

def solve_task1(lines):
    cave = defaultdict(list)
    for line in lines:
        p1, p2 = line.split('-')
        cave[p1].append(p2)
        cave[p2].append(p1)

    paths = getAllPaths('start', 'end', cave)
    return len(paths)

def solve_task2(lines):
    cave = defaultdict(list)
    for line in lines:
        p1, p2 = line.split('-')
        cave[p1].append(p2)
        cave[p2].append(p1)

    paths = getAllPathPart2('start', 'end', cave)
    return len(paths)

if __name__ == '__main__':
    lines = read_lines('input.txt')
    # lines = read_lines('sample.txt')
    print('Task 1:', solve_task1(lines))
    print('Task 2:', solve_task2(lines))
