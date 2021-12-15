from collections import Counter, defaultdict

def read_lines(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]

def solve_task1(lines):
    word = lines[0]
    templates = {line.split(' -> ')[0]: line.split(' -> ')[1] for line in lines[2:]}
    n = 10
    for _ in range(n):
        word = insert_pairs(word, templates)
    c = Counter(word)
    return c.most_common(1)[0][1] - c.most_common()[-1][1]

def insert_pairs(word, templates):
    new_word = ''
    prev_char = ''
    for i in range(len(word)):
        key = f'{prev_char}{word[i]}'
        if key in templates:
            new_word += templates[key]
        new_word += word[i]
        prev_char = word[i]

    return new_word

def solve_task2(lines):
    word = lines[0]
    templates = {line.split(' -> ')[0]: line.split(' -> ')[1] for line in lines[2:]}
    pairs = defaultdict(int)
    for i in range(len(word) - 1):
        key = f'{word[i]}{word[i+1]}'
        pairs[key] += 1
    for _ in range(40):
        new_pairs = defaultdict(int)
        for pair in pairs:
            if pair in templates:
                new_pairs[f'{templates[pair]}{pair[1]}'] += pairs[pair]
                new_pairs[f'{pair[0]}{templates[pair]}'] += pairs[pair]
            else:
                new_pairs[pair] += pairs[pair]
        pairs = new_pairs
    result = defaultdict(int)
    for pair, v in pairs.items():
        result[pair[0]] += v
        result[pair[1]] += v
    print(result)
    result[word[0]] += 1
    result[word[-1]] += 1
    result = Counter(result)
    return (result.most_common(1)[0][1] - result.most_common()[-1][1]) / 2


if __name__ == '__main__':
    lines = read_lines('input.txt')
    # lines = read_lines('sample.txt')
    print('Task 1:', solve_task1(lines))
    print('Task 2:', solve_task2(lines))
