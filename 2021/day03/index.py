from typing import Counter


lines = []
with open('input.txt') as f:
  for l in f:
    lines.append(l.strip())

def solve_task1(lines):
    store = [0] * len(lines[0])
    for line in lines:
        for i, c in enumerate(line):
            if c == '1':
                store[i] += 1
    
    num1 = [1 if s > len(lines) / 2 else 0 for s in store]
    num2 = [ n ^ 1 for n in num1]

    bin_num1 = int(''.join(str(n) for n in num1), 2)
    bin_num2 = int(''.join(str(n) for n in num2), 2)

    print(bin_num1 * bin_num2)

def most_common_bit(nums, position):
    bit_counts = Counter([int(num[position]) for num in nums])
    if bit_counts[0] > bit_counts[1]:
        return 0
    else:
        return 1

def filter(lines, most_common):
    nums = lines[:]
    i = 0
    while len(nums) > 1:
        mcb = most_common_bit(nums, i)
        if not most_common:
            mcb = mcb ^ 1
        nums = [num for num in nums if num[i] == str(mcb)]
        i += 1
    
    return nums[0]

def solve_task2(lines):
    result = int(filter(lines, most_common=True), 2) * int(filter(lines, most_common=False), 2)
    print(result)

solve_task1(lines)
solve_task2(lines)