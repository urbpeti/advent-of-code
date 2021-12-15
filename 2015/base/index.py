class Solver:
    def __init__(self, file_name=None) -> None:
        self.file_name = file_name

    def load_input(self, file_name):
        with open(file_name) as f:
            return f.read().strip().split('\n')

    def solve_task1(self, puzzle_input=None):
        if puzzle_input is None:
            puzzle_input = self.load_input(self.file_name)
        return 0
    
    def solve_task2(self, puzzle_input=None):
        if puzzle_input is None:
            puzzle_input = self.load_input(self.file_name)
        return 0

if __name__ == '__main__':
    s = Solver('input.txt')
    print(s.solve_task1())
    print(s.solve_task2())
