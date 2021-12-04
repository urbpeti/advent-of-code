from typing import Counter

def read_lines(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]

class BingoCard:
    def __init__(self, lines, id):
        self.id = id
        self.lines = lines
        self.seen_numbers = set()
        self.numbers = [int(num) for line in lines for num in line.split()]
        self.columns = [
            set([self.numbers[i*5 + j] for i in range(5)])
            for j in range(5)
        ]
        self.rows = [
            set(self.numbers[i*5: (i + 1)* 5]) for i in range(5)
        ]
        self.to_check = self.columns + self.rows
    
    def check_bingo(self):
        if self.check_columns() or self.check_rows():
            return True
        return False
    
    def check(self):
        for nums in self.to_check:
            if len(nums - self.seen_numbers) == 0:
                return True
        return False
    
    def add_number(self, num):
        self.seen_numbers.add(num)

    def calc_score(self, last_number):
        # sum of all unmarked numbers
        return sum([num for num in self.numbers if num not in self.seen_numbers]) * last_number


    def __str__(self):
        return '\n'.join(self.lines)

class Day4Solver:
    def __init__(self, filename):
        self.lines = read_lines(filename)
        self.tipps = [ int(tipp) for tipp in self.lines[0].split(',') ]
        self.bingo_cards = self.parse_cards(self.lines[2:])
        self.i = 0

    def parse_cards(self, lines):
        cards = []
        card_lines = []
        i = 0
        for line in lines:
            if line == '':
                cards.append(BingoCard(card_lines, i))
                i += 1
                card_lines = []
            else:
                card_lines.append(line)
        
        if card_lines:
            cards.append(BingoCard(card_lines, i))

        return cards

    def solve_task1(self):
        self.i = 0
        while not any([card.check() for card in self.bingo_cards]):
            for card in self.bingo_cards:
                card.add_number(self.tipps[self.i])
            self.i += 1
        
        for card in self.bingo_cards:
            if card.check():
                return card.calc_score(self.tipps[self.i-1])

    def solve_task2(self):
        card_count = len(self.bingo_cards)
        finished = set([card.id for card in self.bingo_cards if card.check()])
        while not all([card.check() for card in self.bingo_cards]):
            for card in self.bingo_cards:
                if card.id in finished:
                    continue
                card.add_number(self.tipps[self.i])
                if card.check():
                    finished.add(card.id)
                    if len(finished) == card_count:
                        return card.calc_score(self.tipps[self.i])
            self.i += 1

        raise Exception('No solution found')        

if __name__ == '__main__':
    solver = Day4Solver('input.txt')
    # solver = Day4Solver('sample.txt')
    print('Task 1:', solver.solve_task1())
    print('Task 2:', solver.solve_task2())