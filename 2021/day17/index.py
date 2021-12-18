import re

def read_lines(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]

def step(pos, vel):
    a_x = -1 if vel[0] > 0 else 0 if vel[0] == 0 else 1
    a_y = -1
    acc = [a_x, a_y]
    pos = [p + v for p, v in zip(pos, vel)]
    vel = [v + a for v, a in zip(vel, acc)]
    return pos, vel

def solve_task1(lines):
    # target area: x=20..30, y=-10..-5
    line = lines[0][len("target area: "):]
    x_range, y_range = line.split(', ')
    x_range = [int(c) for c in x_range[2:].split('..')]
    y_range = [int(c) for c in y_range[2:].split('..')]
    lowest_point = min(y_range)

    best_setting = ([0, 0], 0)
    for vy in range(-abs(lowest_point), abs(lowest_point)):
        pos = [0, 0]
        vel = [0, vy]
        max_y = 0
        while not (vel[1] < 0 and pos[1] < lowest_point):
            pos, vel = step(pos, vel)
            max_y = max(max_y, pos[1])
            if y_range[0] <= pos[1] <= y_range[1]:
                if best_setting[1] < max_y:
                    best_setting = ([0, vy], max_y)
                break
    return best_setting[1]



def solve_task2(lines):
    line = lines[0][len("target area: "):]
    x_range, y_range = line.split(', ')
    x_range = [int(c) for c in x_range[2:].split('..')]
    y_range = [int(c) for c in y_range[2:].split('..')]
    lowest_point = min(y_range)
    x_max = max(x_range)

    possible_setup = []
    for vy in range(-abs(lowest_point), abs(lowest_point)):
        for vx in range(0, x_max + 1):
            pos = [0, 0]
            vel = [vx, vy]
            while not (vel[1] < 0 and pos[1] < lowest_point) and not abs(pos[0]) > abs(x_max):
                pos, vel = step(pos, vel)
                if y_range[0] <= pos[1] <= y_range[1] and x_range[0] <= pos[0] <= x_range[1]:
                    possible_setup.append((vx, vy))
                    break

    return len(possible_setup)
if __name__ == '__main__':
    lines = read_lines('input.txt')
    # lines = read_lines('sample.txt')
    print('Task 1:', solve_task1(lines))
    print('Task 2:', solve_task2(lines))
