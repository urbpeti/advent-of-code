import re
from typing import Counter

class Solver:
    def __init__(self, file_name=None) -> None:
        self.file_name = file_name

    def load_input(self, file_name):
        with open(file_name) as f:
            return f.read().strip().split('\n')

    def is_nice(self, line):
        vowels = ('a', 'e', 'i', 'o', 'u')
        has_double = re.search(r'(.)\1', line)
        vowels_in_line = sum(1 for c in line if c in vowels)
        has_bad_substring = re.search(r'ab|cd|pq|xy', line)
        return has_double and vowels_in_line >= 3 and has_bad_substring is None

    def is_nice2(self, line):
        has_double = re.search(r'(..).*\1', line)
        has_letter_repeat = re.search(r'(.)[^\1]\1', line)
        return has_double and has_letter_repeat

    def solve_task1(self, puzzle_input=None):
        if puzzle_input is None:
            puzzle_input = self.load_input(self.file_name)
        count = 0
        for line in puzzle_input:
            if self.is_nice(line):
                count += 1
        return count
    
    def solve_task2(self, puzzle_input=None):
        if puzzle_input is None:
            puzzle_input = self.load_input(self.file_name)
        count = 0
        for line in puzzle_input:
            if self.is_nice2(line):
                count += 1
        return count

if __name__ == '__main__':
    s = Solver('input.txt')
    print(s.solve_task1())
    print(s.solve_task2())
