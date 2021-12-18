import re
import time
from collections import deque
from itertools import product

class Solver:
    def __init__(self, file_name=None) -> None:
        self.file_name = file_name

    def load_input(self, file_name):
        with open(file_name) as f:
            return f.read().strip().split('\n')

    def reduce_one(self, number):
        q = deque()
        first_part = None
        for i, c in enumerate(number):
            if c == '[':
                q.append(c)
            elif c == ']':
                q.pop()
            if len(q) > 4:
                num = re.search(r'\[(\d+),(\d+)\]', number[i:])
                left, right = int(num.group(1)), int(num.group(2))
                first_part = number[:i]
                second_part = number[i+num.end():]
                first_part_last_number = [m for m in re.finditer(r'(\d+)', first_part)]
                if len(first_part_last_number) > 0:
                    m = first_part_last_number[-1]
                    first_part = first_part[:m.start()] + str(left + int(m.group(1))) + first_part[m.end():]
                last_part_first_number = re.search(r'(\d+)', second_part)
                if last_part_first_number:
                    second_part = second_part[:last_part_first_number.start()] + str(int(last_part_first_number.group(1)) + right) + second_part[last_part_first_number.end():]
                break
        if first_part:
            return f'{first_part}0{second_part}'
        m = re.search(r'([0-9][0-9]+)', number)
        if m:
            n = int(m.group(1))
            return number[:m.start()] + f'[{n//2},{n-n//2}]' + number[m.end():]
        return number

    def reduce_number(self, number):
        prev_number = ""
        while number != prev_number:
            prev_number = number
            number = self.reduce_one(number)
        return number
    
    def add_numbers(self, numbers):
        num = numbers[0]
        for n in numbers[1:]:
            num = f'[{num},{n}]'
            num = self.reduce_number(num)
        return num

    def magnitude(self, number):
        m = re.match(r'^(\d+)$', number)
        if m:
            return int(m.group(1))
        level = 0
        for i, c in enumerate(number):
            if c == '[':
                level += 1
            elif c == ']':
                level -= 1
            if c == ',' and level == 1:
                return self.magnitude(number[1:i]) * 3 + self.magnitude(number[i+1:-1]) * 2
        raise Exception(f"Invalid number {number}") 

    def solve_task1(self, puzzle_input=None):
        if puzzle_input is None:
            puzzle_input = self.load_input(self.file_name)
        num = self.add_numbers(puzzle_input)
        return self.magnitude(num)
    
    def solve_task2(self, puzzle_input=None):
        if puzzle_input is None:
            puzzle_input = self.load_input(self.file_name)
        max_magnitute = 0
        nums = product(puzzle_input, puzzle_input)
        for n1, n2 in nums:
            if n1 == n2:
                continue
            mag = self.magnitude(self.add_numbers([n1, n2]))
            if mag > max_magnitute:
                max_magnitute = mag
        return max_magnitute

if __name__ == '__main__':
    s = Solver('input.txt')
    start = time.time()
    print(f"Task 1: {s.solve_task1()} took {time.time() - start:.3f} sec")
    start2 = time.time()
    print(f"Task 2: {s.solve_task2()} took {time.time() - start2:.3f} sec")
    print(f"Total: {time.time() - start:.3f} sec")
