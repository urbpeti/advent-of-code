import time

def read_lines(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]

def turn(p, d, rolled):
    pos = p[0]
    new_pos = (pos + 3 * d + 3)
    new_pos = new_pos % 10
    return ((new_pos, p[1] + new_pos + 1), d + 3, rolled + 3)

def solve_task1(lines):
    p1_pos = int(lines[0].split(' ')[-1])
    p2_pos = int(lines[1].split(' ')[-1])
    p1 = (p1_pos - 1, 0)
    p2 = (p2_pos - 1, 0)
    die = 1
    rolled = 0
    while True:
        p1, die, rolled = turn(p1, die, rolled)
        if p1[1] >= 1000:
            break
        p1, p2 = p2, p1
    return p2[1] * rolled

cache = {}
def play_game(p1, p2, p1_turn):
    if (p1, p2, p1_turn) in cache:
        return cache[(p1, p2, p1_turn)]
    p1_wins = 0
    p2_wins = 0
    if p1[1] >= 21 or p2[1] >= 21:
        p1_wins += 1 if p1[1] > p2[1] else 0
        p2_wins += 1 if p2[1] > p1[1] else 0
        return p1_wins, p2_wins

    if p1_turn:
        p1_turns = turn2(p1)
        for p1_turn in p1_turns:
            times = p1_turn[2]
            p1_turn = (p1_turn[0], p1_turn[1])
            p1_win, p2_win = play_game(p1_turn, p2, not p1_turn)
            p1_wins += p1_win * times
            p2_wins += p2_win * times
    else:
        p2_turns = turn2(p2)
        for p2_turn in p2_turns:
            times = p2_turn[2]
            p2_turn = (p2_turn[0], p2_turn[1])
            p1_win, p2_win = play_game(p1, p2_turn, not p1_turn)
            p1_wins += p1_win * times
            p2_wins += p2_win * times
    cache[(p1, p2, p1_turn)] = (p1_wins, p2_wins)
    return p1_wins, p2_wins

def turn2(p):
    ds = [3, 4, 5, 6, 7, 8, 9]
    ts = [1, 3, 6, 7, 6, 3, 1]
    pos = p[0]
    new_pos = []
    for d, t in zip(ds, ts):
        new_p = (pos + d) % 10
        new_pos.append((new_p, p[1] + new_p + 1, t))
    return new_pos

def solve_task2(lines):
    p1_pos = int(lines[0].split(' ')[-1])
    p2_pos = int(lines[1].split(' ')[-1])
    p1 = (p1_pos - 1, 0)
    p2 = (p2_pos - 1, 0)
    p1_wins, p2_wins = play_game(p1, p2, True)
    return p1_wins if p1_wins > p2_wins else p2_wins

if __name__ == '__main__':
    lines = read_lines('input.txt')
    # lines = read_lines('sample.txt')
    print('Task 1:', solve_task1(lines))
    st = time.time()
    print('Task 2:', solve_task2(lines))
    print('Time:', time.time() - st)
