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
        directions = {
            '^': (0, 1),
            'v': (0, -1),
            '<': (-1, 0),
            '>': (1, 0)
        }
        pos = (0, 0)
        houses = {pos: 1}
        for char in iter(puzzle_input):
            pos = tuple(map(sum, zip(pos, directions[char])))
            if pos not in houses:
                houses[pos] = 1
            else:
                houses[pos] += 1

        return len(houses)
    
    def solve_task2(self, puzzle_input=None):
        if puzzle_input is None:
            puzzle_input = self.load_input(self.file_name)
        puzzle_input = puzzle_input[0]
        directions = {
            '^': (0, 1),
            'v': (0, -1),
            '<': (-1, 0),
            '>': (1, 0)
        }
        santa_pos = (0, 0)
        robot_pos = (0, 0)
        houses = {santa_pos: 1}
        i = 0
        for char in iter(puzzle_input):
            if i % 2 == 0:
                p = santa_pos
            else:
                p = robot_pos
            pos = tuple(map(sum, zip(p, directions[char])))
            if pos not in houses:
                houses[pos] = 1
            else:
                houses[pos] += 1
            
            if i % 2 == 0:
                santa_pos = pos
            else:
                robot_pos = pos
            i += 1

        return len(houses)

if __name__ == '__main__':
    s = Solver('input.txt')
    print(s.solve_task1())
    print(s.solve_task2())
