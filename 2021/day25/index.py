import time

def read_lines(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]

def step_char(field, char):
    new_field = [['.'] * len(field[0]) for _ in range(len(field))]
    for y in range(len(field)):
        for x in range(len(field[0])):
            if field[y][x] == char:
                continue
            new_field[y][x] = field[y][x]
    if char == '>':
        for y in range(len(field)):
            for x in range(len(field[0])):
                if field[y][x] == '>':
                    key = (x + 1) % len(field[0])
                    if field[y][key] == '.':
                        new_field[y][key] = '>'
                    else:
                        new_field[y][x] = '>'
    else:
        for y in range(len(field)):
            for x in range(len(field[0])):
                if field[y][x] == 'v':
                    key = (y + 1) % len(field)
                    if field[key][x] == '.':
                        new_field[key][x] = 'v'
                    else:
                        new_field[y][x] = 'v'
    return new_field

def step(field):
    new_field = step_char(field, '>')
    new_field = step_char(new_field, 'v')
    return new_field

def print_field(field):
    for row in field:
        print(''.join(row))
    print()

def get_field_hash(field):
    return ''.join([''.join(row) for row in field])

def solve_task1(lines):
    field = lines
    new_field = step(field)
    i = 1
    while get_field_hash(field) != get_field_hash(new_field):
        field = new_field
        new_field = step(field)
        i += 1
    return i

def solve_task2(lines):
    return 0


if __name__ == '__main__':
    lines = read_lines('input.txt')
    # lines = read_lines('sample.txt')
    print('Task 1:', solve_task1(lines))
