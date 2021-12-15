import heapq as hq

def read_lines(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]

def smallest_cost_path(field, start, end):
    ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    Q = []
    dist = {(i, j): float('inf') for j in range(len(field[0])) for i in range(len(field)) }
    dist[start] = 0
    visited = set()
    hq.heappush(Q, (0, start))
    while Q:
        i, j = hq.heappop(Q)[1]
        visited.add((i, j))

        for d in ds:
            ni, nj = i + d[0], j + d[1]
            if 0 <= ni < len(field) and 0 <= nj < len(field[0]):
                if (ni, nj) not in visited:
                    alt = dist[(i, j)] + field[ni][nj]
                    if alt < dist[(ni, nj)]:
                        hq.heappush(Q, (alt, (ni, nj)))
                        dist[(ni, nj)] = alt
    return dist[end]

def solve_task1(lines):
    field = [[int(c) for c in list(line)] for line in lines]
    cost = smallest_cost_path(field, (0, 0), (len(field) - 1, len(field[0]) - 1))
    return cost

def cost_of_path(field, start, end, level):
    level_field = [[(field[i][j] + level) % 10 for j in range(len(field[0]))] for i in range(len(field))]
    return smallest_cost_path(level_field, start, end)

def solve_task2(lines):
    old_field = [[int(c) for c in list(line)] for line in lines]
    field = []
    for i in range(5):
        for r in old_field:
            new_row = []
            for j in range(5):
                for c in r:
                    v = (c + i + j) % 10 + (c + i + j) // 10
                    new_row.append(v)
            field.append(new_row)
    cost = cost_of_path(field, (0, 0), (len(field) - 1, len(field[0]) - 1), 0)
    return cost

if __name__ == '__main__':
    lines = read_lines('input.txt')
    # lines = read_lines('sample.txt')
    print('Task 1:', solve_task1(lines))
    print('Task 2:', solve_task2(lines))
