from collections import defaultdict, deque

def read_lines(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]

def parse_lines(lines):
    dots = {}
    folds = []
    for line in lines:
        if not line:
            continue
        if line.startswith('fold along '):
            value = int(line[line.index('=') + 1:])
            axis = line[line.index('=') - 1:line.index('=')]
            folds.append((axis, value))
            continue
        x, y = line.split(',')
        x, y = int(x), int(y)
        dots[(x, y)] = True
    return dots, folds

def fold(dots, axis, value):
    new_dots = {}
    if axis == 'x':
        for dot in dots:    
            x, y = dot
            if x <= value:
                new_dots[(x, y)] = True
            elif x == value:
                continue
            else:
                new_dots[(value - (x - value)), y] = True
    elif axis == 'y':
        for dot in dots:
            x, y = dot
            if y < value:
                new_dots[(x, y)] = True
            elif y == value:
                continue
            else:
                new_dots[(x, value - (y - value))] = True
    else:
        raise Exception('invalid axis')
    return new_dots

def solve_task1(lines):
    dots, folds = parse_lines(lines)
    axis, value = folds[0]
    dots = fold(dots, axis, value)
    return len(dots)

def solve_task2(lines):
    dots, folds = parse_lines(lines)
    for axis, value in folds:
        dots = fold(dots, axis, value)
    maxline = (max([k[0] for k in dots.keys()]), max([k[1] for k in dots.keys()]))
    for y in range(maxline[1] + 1):
        for x in range(maxline[0] + 1):
            if (x, y) in dots:
                print('#', end='')
            else:
                print('.', end='')
        print()
            
    return ''

if __name__ == '__main__':
    lines = read_lines('input.txt')
    # lines = read_lines('sample.txt')
    print('Task 1:', solve_task1(lines))
    print('Task 2:')
    solve_task2(lines)
