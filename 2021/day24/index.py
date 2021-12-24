import time

def read_lines(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]

operator = {
    'mul': lambda x, y: x * y,
    'add': lambda x, y: x + y,
    'mod': lambda x, y: x % y,
    'div': lambda x, y: x // y,
    'eql': lambda x, y: 1 if x == y else 0,
}

def evaluate(lines, regs, input_values=""):
    i = 0
    for line in lines:
        cmd = line.split(' ')
        if cmd[0] == 'inp':
            regs[cmd[1]] = int(input_values[i])
            i += 1
        else:
            n = regs[cmd[2]] if cmd[2].isalpha() else int(cmd[2])
            regs[cmd[1]] = operator[cmd[0]](regs[cmd[1]], n)
        # print(f'{line} {regs}')

    return regs

def solve_task1(lines):
    regs = {'x': 0, 'y': 0, 'z': 0, 'w': 0}
    numbers = f'91297395919993'
#               abcddeffggecba
# a - 6
# b + 8
# c + 7
# d - 2
# e + 6
# f - 4
# g - 8
    regs = evaluate(lines[:18 * len(numbers)], regs, numbers)
    assert regs['z'] == 0
    return numbers

def solve_task2(lines):
    regs = {'x': 0, 'y': 0, 'z': 0, 'w': 0}
    numbers = f'71131151917891'
#               abcddeffggecba
# a - 6
# b + 8
# c + 7
# d - 2
# e + 6
# f - 4
# g - 8
    regs = evaluate(lines[:18 * len(numbers)], regs, numbers)
    assert regs['z'] == 0
    return numbers


if __name__ == '__main__':
    # lines = read_lines('input.txt')
    lines = read_lines('sample.txt')
    print('Task 1:', solve_task1(lines))
    st = time.time()
    print('Task 2:', solve_task2(lines))
    print('Time:', time.time() - st)
