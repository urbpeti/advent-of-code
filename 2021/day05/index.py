def read_lines(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]

class Day5Solver:
    def __init__(self, filename):
        self.field = {}
        self.lines = read_lines(filename)

    def add_line_to_filed(self, start, end):
        start_x, start_y = start
        end_x, end_y = end

        d_x, d_y = end_x - start_x, end_y - start_y
        d_x = d_x / abs(d_x) if d_x != 0 else 0
        d_y = d_y / abs(d_y) if d_y != 0 else 0
        while start_x != end_x or start_y != end_y:
            key = (start_x, start_y)
            if key not in self.field:
                self.field[key] = 0
            self.field[key] = self.field[key] + 1
            start_x = start_x + d_x
            start_y = start_y + d_y
        
        key = (end_x, end_y)
        if key not in self.field:
            self.field[key] = 0
        self.field[key] = self.field[key] + 1

    def solve_task1(self):
        for line in self.lines:
        # line: 0,9 -> 5,9
            start_x, start_y = [int(x) for x in line.split('->')[0].split(',')]
            end_x, end_y = [int(x) for x in line.split('->')[1].split(',')]

            if start_x != end_x and start_y != end_y:
                continue
            
            self.add_line_to_filed((start_x, start_y), (end_x, end_y))
        
        return len([ x for x in self.field.values() if x >= 2 ])

    def print_field(self):
        for y in range(10):
            for x in range(10):
                if (x, y) in self.field:
                    print(self.field[(x, y)], end='')
                else:
                    print('.', end='')
            print()

    def solve_task2(self):
        for line in self.lines:
            start_x, start_y = [int(x) for x in line.split('->')[0].split(',')]
            end_x, end_y = [int(x) for x in line.split('->')[1].split(',')]

            if start_x == end_x or start_y == end_y:
                continue

            self.add_line_to_filed((start_x, start_y), (end_x, end_y))

        return len([ x for x in self.field.values() if x >= 2 ])

if __name__ == '__main__':
    solver = Day5Solver('input.txt')
    # solver = Day5Solver('sample.txt')
    print('Task 1:', solver.solve_task1())
    print('Task 2:', solver.solve_task2())
