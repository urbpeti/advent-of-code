import time

def read_lines(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]

def filter_rules(rules, x_range, y_range, z_range):
    return [
        (
        [max(rule[0][0], x_range[0]), min(rule[0][1], x_range[1])],
        [max(rule[1][0], y_range[0]), min(rule[1][1], y_range[1])],
        [max(rule[2][0], z_range[0]), min(rule[2][1], z_range[1])], rule[3]) for rule in rules
        if not (rule[0][1] < x_range[0] or rule[0][0] > x_range[1]) and 
           not (rule[1][1] < y_range[0] or rule[1][0] > y_range[1]) and
           not (rule[2][1] < z_range[0] or rule[2][0] > z_range[1])
    ]

def count_element_in_region(rules, x_range, y_range, z_range):
    if x_range[0] > x_range[1] or y_range[0] > y_range[1] or z_range[0] > z_range[1]:
        return 0
    rules_for_region = filter_rules(rules, x_range, y_range, z_range)
    if len(rules_for_region) == 0:
        return 0
    
    if all(rule[0][0] == x_range[0] and rule[0][1] == x_range[1] and 
              rule[1][0] == y_range[0] and rule[1][1] == y_range[1] and
              rule[2][0] == z_range[0] and rule[2][1] == z_range[1] for rule in rules_for_region):
        if rules_for_region[-1][3] == 'on':
            return (x_range[1] - x_range[0] + 1) * (y_range[1] - y_range[0] + 1) * (z_range[1] - z_range[0] + 1)
        else:
            return 0

    summa = 0
    for rule in rules_for_region:
        if not (rule[0][0] == x_range[0] and rule[0][1] == x_range[1] and 
              rule[1][0] == y_range[0] and rule[1][1] == y_range[1] and
              rule[2][0] == z_range[0] and rule[2][1] == z_range[1]):
            if rule[0][0] > x_range[0]:
                summa += count_element_in_region(rules, (x_range[0], rule[0][0] - 1), y_range, z_range)
                summa += count_element_in_region(rules, (rule[0][0],  x_range[1]), y_range, z_range)
            elif rule[0][1] < x_range[1]:
                summa += count_element_in_region(rules, (rule[0][1] + 1, x_range[1]), y_range, z_range)
                summa += count_element_in_region(rules, (x_range[0], rule[0][1]), y_range, z_range)
            elif rule[1][0] > y_range[0]:
                summa += count_element_in_region(rules, x_range, (y_range[0], rule[1][0] - 1), z_range)
                summa += count_element_in_region(rules, x_range, (rule[1][0],  y_range[1]), z_range)
            elif rule[1][1] < y_range[1]:
                summa += count_element_in_region(rules, x_range, (rule[1][1] + 1, y_range[1]), z_range)
                summa += count_element_in_region(rules, x_range, (y_range[0], rule[1][1]), z_range)
            elif rule[2][0] > z_range[0]:
                summa += count_element_in_region(rules, x_range, y_range, (z_range[0], rule[2][0] - 1))
                summa += count_element_in_region(rules, x_range, y_range, (rule[2][0],  z_range[1]))
            elif rule[2][1] < z_range[1]:
                summa += count_element_in_region(rules, x_range, y_range, (rule[2][1] + 1, z_range[1]))
                summa += count_element_in_region(rules, x_range, y_range, (z_range[0], rule[2][1]))
            break
    return summa


def solve_task1(lines):
    rules = []
    for line in lines:
        switch = line.split(' ')[0]
        rule = line.split(' ')[1]
        x, y, z = [[int(y) for y in x[2:].split('..')] for x in rule.split(',')]
        rules.append((x, y, z, switch))
    elements = count_element_in_region(rules, (-50, 50), (-50, 50), (-50, 50))
    return elements

def solve_task2(lines):
    rules = []
    for line in lines:
        switch = line.split(' ')[0]
        rule = line.split(' ')[1]
        x, y, z = [[int(y) for y in x[2:].split('..')] for x in rule.split(',')]
        rules.append((x, y, z, switch))
    x_low = min([rule[0][0] for rule in rules])
    x_high = max([rule[0][1] for rule in rules])
    y_low = min([rule[1][0] for rule in rules])
    y_high = max([rule[1][1] for rule in rules])
    z_low = min([rule[2][0] for rule in rules])
    z_high = max([rule[2][1] for rule in rules])
    elements = count_element_in_region(rules, (x_low, x_high), (y_low, y_high), (z_low, z_high))
    return elements

if __name__ == '__main__':
    lines = read_lines('input.txt')
    # lines = read_lines('sample.txt')
    print('Task 1:', solve_task1(lines))
    st = time.time()
    print('Task 2:', solve_task2(lines))
    print('Time:', time.time() - st)
