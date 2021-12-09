def read_lines(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]

def sum_of_numbers_from_zero(number):
    return int((number / 2) * (number + 1))

def solve_task1(lines):
    count = 0
    for line in lines:
        numbers = line.split(' | ')[0].split(' ')
        displays = line.split(' | ')[1].split(' ')
        count += len([d for d in displays if len(d) in [2, 3, 4, 7]])
    return count

def solve_task2(lines):
    count = 0
    for line in lines:
        numbers = line.split(' | ')[0].split(' ')
        mapping = deduction(numbers)
        displays = line.split(' | ')[1].split(' ')
        number = [mapping[''.join(sorted(d))] for d in displays]
        number = sum([ 10 ** i * n for i, n in enumerate(reversed(number))])
        count += number
    return count

def deduction(numbers):
    mapping = {}
    for number in numbers[:]:
        if len(number) == 2:
            mapping[1] = set(number)
            numbers.remove(number)
        elif len(number) == 3:
            mapping[7] = set(number)
            numbers.remove(number)
        elif len(number) == 4:
            mapping[4] = set(number)
            numbers.remove(number)
        elif len(number) == 7:
            mapping[8] = set(number)
            numbers.remove(number)
    
    # 3
    for number in numbers[:]:
        n = set(number)
        if len(n - mapping[1]) == 3:
            mapping[3] = n
            numbers.remove(number)
    # 9
    for number in numbers[:]:
        n = set(number)
        if len(n & mapping[4]) == 4:
            mapping[9] = n
            numbers.remove(number)
    # 6
    for number in numbers[:]:
        n = set(number)
        if len(n) == 6 and len(n & mapping[1]) == 1:
            mapping[6] = set(number)
            numbers.remove(number)
    # 0
    for number in numbers[:]:
        if len(number) == 6:
            mapping[0] = set(number)
            numbers.remove(number)
    # 2
    for number in numbers[:]:
        n = set(number)
        if len(n & mapping[4]) == 2:
            mapping[2] = set(number)
            numbers.remove(number)
    
    assert len(numbers) == 1
    # 5
    mapping[5] = set(numbers[0])
    return { ''.join(sorted(v)): k for k, v in mapping.items() }


if __name__ == '__main__':
    lines = read_lines('input.txt')
    # lines = read_lines('sample.txt')
    print('Task 1:', solve_task1(lines))
    print('Task 2:', solve_task2(lines))
