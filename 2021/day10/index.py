from collections import deque

def read_lines(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]

def is_correct(line):
    pairs = {
        '}': '{',
        ']': '[',
        ')': '(',
        '>': '<'
    }
    stack = deque()
    for c in line:
        if c not in pairs.keys():
            stack.append(c)
        else:
            last = stack.pop()
            if last != pairs[c]:
                return False, c
    return True, None


def solve_task1(lines):
    char_poinst = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    res = 0
    for line in lines:
        correct, wrong_char = is_correct(line)
        if not correct:
            res += char_poinst[wrong_char]
    
    return res

def solve_task2(lines):
    char_values = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4,
    }
    correct_lines = [line for line in lines if is_correct(line)[0]]
    scores = []
    for line in correct_lines:
        to_complete = finish_line(line)
        score = 0
        for i, c in enumerate(to_complete):
            score *= 5
            score += char_values[c]
        scores.append(score)
    print(scores)
    return sorted(scores)[len(scores)//2]

def finish_line(line):
    stack = deque()
    for c in line:
        if c in ['{', '[', '(', '<']:
            stack.append(c)
        else:
            stack.pop()
    return ''.join(reversed(stack))

if __name__ == '__main__':
    lines = read_lines('input.txt')
    # lines = read_lines('sample.txt')
    print('Task 1:', solve_task1(lines))
    print('Task 2:', solve_task2(lines))
