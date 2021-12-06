from collections import Counter, defaultdict


def read_lines(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]

class Day5Solver:
    def __init__(self, filename):
        self.lines = read_lines(filename)

    def solve_task1(self):
        initial = Counter([ int(x) for x in self.lines[0].split(',')])
        state = initial.copy()
        for i in range(80):
            new_state = defaultdict(lambda: 0)
            for k, v in state.items():
                if k == 0:
                    new_state[8] += v
                    new_state[6] += v
                else:
                    new_state[k - 1] += v
            state = new_state
        return sum(state.values())

    def solve_task2(self):
        initial = Counter([ int(x) for x in self.lines[0].split(',')])
        state = initial.copy()
        dead = 0
        for i in range(256):
            new_state = defaultdict(lambda: 0)
            for k, v in state.items():
                if k == 0:
                    new_state[8] += v
                    new_state[6] += v
                    dead += v
                else:
                    new_state[k - 1] += v
            state = new_state
        return sum(state.values())

if __name__ == '__main__':
    solver = Day5Solver('input.txt')
    # solver = Day5Solver('sample.txt')
    print('Task 1:', solver.solve_task1())
    print('Task 2:', solver.solve_task2())
