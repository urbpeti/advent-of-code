from collections import Counter, defaultdict


def read_lines(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]

def calc_best_position_cost(nums, cost_func):
    best_pos = -1
    best_value = float('inf')
    while True:
        next_best = sum([cost_func(n, best_pos) for n in nums])
        if next_best >= best_value:
            break
        best_value = next_best
        best_pos += 1
    return best_value

def sum_of_numbers_from_zero(number):
    return int((number / 2) * (number + 1))

def solve_task1(nums):
    return calc_best_position_cost(nums, lambda n, pos: abs(n - pos))

def solve_task2(nums):
    return calc_best_position_cost(nums, lambda n, pos: sum_of_numbers_from_zero(abs(n - pos)))

if __name__ == '__main__':
    lines = read_lines('input.txt')
    # lines = read_lines('sample.txt')
    nums = [int(line) for line in lines[0].split(',')]
    print('Task 1:', solve_task1(nums))
    print('Task 2:', solve_task2(nums))
