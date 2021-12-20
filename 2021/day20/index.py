import re

def read_lines(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]

def calc_new_char(image, y, x, iea):
    ds = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
    number = ''
    for d in ds:
        if image[y + d[0]][x + d[1]] == '#':
            number += '1'
        else:
            number += '0'
    return iea[int(number, 2)]

def step(image, iea, even):
    padding = '.' if even else '#'
    image_with_padding = [padding * len(image[0])] * 2 + image + [padding * len(image[0])] * 2
    for i, line in enumerate(image_with_padding):
        image_with_padding[i] = padding * 2 + line + padding * 2

    new_image = []
    for y in range(1, len(image_with_padding) - 1):
        new_row = []
        for x in range(1, len(image_with_padding[y]) -1):
            c = calc_new_char(image_with_padding, y, x, iea)
            new_row.append(c)
        new_image.append(''.join(new_row))
    return new_image


def solve_task1(lines):
    iea = lines[0]
    image = lines[2:]
    for i in range(2):
        image = step(image, iea, i % 2 == 0 or iea[0] == '.')
    res = sum([r.count('#') for r in image])
    return res

def solve_task2(lines):
    iea = lines[0]
    image = lines[2:]
    for i in range(50):
        image = step(image, iea, i % 2 == 0 or iea[0] == '.')
    res = sum([r.count('#') for r in image])
    return res

if __name__ == '__main__':
    lines = read_lines('input.txt')
    # lines = read_lines('sample.txt')
    print('Task 1:', solve_task1(lines))
    print('Task 2:', solve_task2(lines))
