from collections import deque

def read_lines(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]

def step(field):
    ds = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    flashed = set()
    cells = deque([(y, x) for y in range(len(field)) for x in range(len(field[0]))])
    while cells:
        y, x = cells.pop()
        field[y][x] += 1
        c = field[y][x]
        if c > 9 and (y, x) not in flashed:
            flashed.add((y, x))
            for dy, dx in ds:
                if 0 <= y + dy < len(field) and 0 <= x + dx < len(field[0]):
                    cells.appendleft((y + dy, x + dx))
    
    for y in range(len(field)):
        for x in range(len(field[0])):
            if field[y][x] > 9:
                field[y][x] = 0
    
    return len(flashed)
            


def solve_task1(lines):
    field = [[int(c) for c in line] for line in lines]
    flashed = 0
    for i in range(100):
        flashed += step(field)
    for line in field:
        print(' '.join(f'{c:2}' for c in line))
    return flashed

def solve_task2(lines):
    field = [[int(c) for c in line] for line in lines]
    i = 0
    while not all([c == 0 for line in field for c in line]):
        step(field)
        i += 1
    return i

if __name__ == '__main__':
    lines = read_lines('input.txt')
    # lines = read_lines('sample.txt')
    print('Task 1:', solve_task1(lines))
    print('Task 2:', solve_task2(lines))
