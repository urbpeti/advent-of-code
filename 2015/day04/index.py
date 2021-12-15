import hashlib

class Solver:
    def __init__(self, file_name=None) -> None:
        self.file_name = file_name

    def load_input(self, file_name):
        with open(file_name) as f:
            return f.read().strip().split('\n')

    def solve_task1(self, puzzle_input=None):
        if puzzle_input is None:
            puzzle_input = self.load_input(self.file_name)
        puzzle_input = puzzle_input[0]
        return self.find_number_for(puzzle_input, 5)

        
    def find_number_for(self, string, n):
        i = 0
        while True:
            i += 1
            md5 = hashlib.md5((string + str(i)).encode('utf-8')).hexdigest()
            if md5[:n] == '0' * n:
                print(md5)
                return i
    
    def solve_task2(self, puzzle_input=None):
        if puzzle_input is None:
            puzzle_input = self.load_input(self.file_name)
        puzzle_input = puzzle_input[0]
        return self.find_number_for(puzzle_input, 6)

if __name__ == '__main__':
    s = Solver('input.txt')
    print(s.solve_task1())
    print(s.solve_task2())
