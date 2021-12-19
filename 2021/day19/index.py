import time

def read_lines(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]

def read_scanners(lines):
    scanners = []
    scanner = []
    for line in lines:
        if line == '':
            scanners.append(scanner)
            scanner = []
            continue
        if not line.startswith('---'):
            x, y, z = [int(c) for c in line.split(',')]
            scanner.append((x, y, z))
    if scanner:
        scanners.append(scanner)
    return scanners

def rotateZ(vec, times):
    for i in range(times):
        vec = (vec[1], -vec[0], vec[2])
    return vec

def rotateX(vec, times):
    for i in range(times):
        vec = (vec[0], -vec[2], vec[1])
    return vec

def rotateY(vec, times):
    for i in range(times):
        vec = (-vec[2], vec[1], vec[0])
    return vec

def orient(vec, orientation):
    if 16 <= orientation < 24:
        orientation -= 16
        vec = rotateY(vec, 1)
    if 8 <= orientation < 16:
        orientation -= 8
        vec = rotateX(vec, 1)
    if 4 <= orientation < 8:
        vec = (vec[0], -vec[1], -vec[2])
    return rotateZ(vec, orientation)

orientation_cache = {}
def get_orientation(scanners, rotation):
    i, s = scanners
    if (i, rotation) in orientation_cache:
        return orientation_cache[(i, rotation)]
    oriented_scanner = [orient(v, rotation) for v in s]
    orientation_cache[(i, rotation)] = oriented_scanner 
    return oriented_scanner

def pair_same_bacons(sc1_with_index, sc2_with_index):
    scanners1 = sc1_with_index[1]
    for base1 in list(scanners1)[:-11]:
        sc1 = set([(x - base1[0], y - base1[1], z - base1[2]) for x, y, z in scanners1])
        for rotation in range(24):
            oriented_scanner = get_orientation(sc2_with_index, rotation)
            for i, base2 in enumerate(oriented_scanner):
                sc2_new = set([(x - base2[0], y - base2[1], z - base2[2]) for x, y, z in oriented_scanner])
                if len(sc1 & sc2_new) >= 12:
                    return True, base1, sc2_with_index[1][i], rotation
    return False, (0, 0, 0), (0, 0, 0), 0

def add_vec3(vec1, vec2):
    return (vec1[0] + vec2[0], vec1[1] + vec2[1], vec1[2] + vec2[2])

def sub_vec3(vec1, vec2):
    return (vec1[0] - vec2[0], vec1[1] - vec2[1], vec1[2] - vec2[2])
                
def solve_task1(lines):
    scanners = read_scanners(lines)
    scanners = [(i, scanner) for i, scanner in enumerate(scanners)]
    all_scanners = len(scanners)
    region = [(0, set(scanners[0][1]))]
    scanners.pop(0)
    visited_pair = set()
    scanner_locations = [(0, 0, 0)]
    while scanners:
        for i, s in scanners:
            found = False
            for j, r in region:
                if (i, j) in visited_pair:
                    continue
                visited_pair.add((i, j))
                pair, b1, b2, rotation = pair_same_bacons((j, r), (i, s))
                if pair:
                    sc2 = set([add_vec3(orient((x - b2[0], y - b2[1], z - b2[2]), rotation), b1) for x, y, z in s])
                    region.append((i, sc2))
                    scanners.remove((i, s))
                    scanner_locations.append(sub_vec3(orient(b2, rotation), b1))
                    found = True
                    break
            if found:
                break
        print(f'{len(region)}/{all_scanners} has found')
    fields = set()
    for r in [r[1] for r in region]:
        fields |= r
    return len(fields), scanner_locations

def vec3_mannhattan(vec1, vec2):
    return abs(vec1[0] - vec2[0]) + abs(vec1[1] - vec2[1]) + abs(vec1[2] - vec2[2])

def solve_task2(scanner_locations):
    max_distance = 0
    for i in range(len(scanner_locations)):
        for j in range(i + 1, len(scanner_locations)):
            d = vec3_mannhattan(scanner_locations[i], scanner_locations[j])
            if d > max_distance:
                max_distance = d
    return max_distance

if __name__ == '__main__':
    lines = read_lines('input.txt')
    # lines = read_lines('sample.txt')
    start_time = time.time()
    task1_solution, scanner_locations = solve_task1(lines)
    print(f'Task 1: {task1_solution} found in {time.time() - start_time:.2f}s')
    start2 = time.time()
    print(f'Task 2: {solve_task2(scanner_locations)} found in {time.time() - start2:.2f}s')
    print(f'Total: {time.time() - start_time:.2f}s')
