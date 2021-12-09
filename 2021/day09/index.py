from collections import deque

def read_lines(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]

def sum_of_numbers_from_zero(number):
    return int((number / 2) * (number + 1))

def find_basins(field):
    basins = []
    for row in range(len(field)):
        for col in range(len(field[row])):
            ds = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            neightbours = [ (row + d[0], col + d[1]) for d in ds if 0 <= row + d[0] < len(field) and 0 <= col + d[1] < len(field[row])]
            if all([field[row][col] < field[nrow][ncol] for nrow, ncol in neightbours]):
                basins.append((row, col))
    return basins

def solve_task1(lines):
    field = [[int(c) for c in list(line)] for line in lines]
    return sum([field[row][col] + 1 for row, col in find_basins(field)])

def solve_task2(lines):
    field = [[int(c) for c in list(line)] for line in lines]


    basins = find_basins(field)
    basin_sizes = [calc_basin_size(field, row, col) for row, col in basins]
    res = 1
    for size in sorted(basin_sizes)[-3:]:
        res *= size
    return res

def calc_basin_size(field, row, col):
    ds = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    seen = set()
    q = deque([(row, col, -1)])
    basin_cells = set()
    while q:
        r, c, prev = q.popleft()
        if (r, c, prev) in seen or (r, c) in basin_cells:
            continue
        if field[r][c] < prev or field[r][c] == 9:
            continue
        basin_cells.add((r, c))
        seen.add((r, c, prev))
        neightbours = [ (r + d[0], c + d[1]) for d in ds if 0 <= r + d[0] < len(field) and 0 <= c + d[1] < len(field[r])]
        for nrow, ncol in neightbours:
            q.append((nrow, ncol, field[r][c]))
    
    return len(basin_cells)

if __name__ == '__main__':
    lines = read_lines('input.txt')
    # lines = read_lines('sample.txt')
    print('Task 1:', solve_task1(lines))
    print('Task 2:', solve_task2(lines))
