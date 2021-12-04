lines = []
with open('input.txt') as f:
  for l in f:
    lines.append(l.strip())

def solve_task1(lines):
    depth = 0
    horizontal = 0
    for l in lines:
        n = int(l.split(' ')[1])
        if l.startswith('f'):
            horizontal += n
        elif l.startswith('u'):
            depth -= n
        elif l.startswith('d'):
            depth += n
    print(depth * horizontal)

def solve_task2(lines):
    depth = 0
    aim = 0
    horizontal = 0
    for l in lines:
        n = int(l.split(' ')[1])
        if l.startswith('f'):
            horizontal += n
            depth += aim * n
        elif l.startswith('u'):
            aim -= n
        elif l.startswith('d'):
            aim += n
    print(depth * horizontal)

solve_task1(lines)
solve_task2(lines)