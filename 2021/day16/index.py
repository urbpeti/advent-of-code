def read_lines(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]

m = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

def get_version(line):
    return line[3:], int(line[:3], 2)

def get_packet_type(line):
    return line[3:], int(line[:3], 2)

def take(line, n):
    return line[n:], int(line[:n], 2)

def parse_literal(line):
    numbers = ''
    number = line[:5]
    line = line[5:]
    while number[0] != '0':
        number = number[1:]
        numbers += number
        
        number = line[:5]
        line = line[5:]
    number = number[1:]
    numbers += number
    return line, int(numbers, 2)

def parse_packet(line):
    line, version = take(line, 3)
    line, packet_type = take(line, 3)
    if packet_type == 4:
        line, number = parse_literal(line)
        return line, (version, packet_type, number)

    line, t = take(line, 1)
    result = []
    if t == 0:
        line, L = take(line, 15)
        original_length = len(line)
        while original_length - len(line) < L:
            line, sub_packets = parse_packet(line)
            result.append(sub_packets)
    else:
        line, L = take(line, 11)
        for n in range(L):
            line, sub_packets = parse_packet(line)
            result.append(sub_packets)
    return line, (version, packet_type, result)

def get_sum_versions(packet, sum):
    version, packet_type, sub_packets = packet
    sum += version
    if isinstance(sub_packets, list):
        for sub_packet in sub_packets:
            sum = get_sum_versions(sub_packet, sum)
    
    return sum

def solve_task1(lines):
    line = lines[0]
    binary = "".join([m[c] for c in line])
    line, packet = parse_packet(binary)
    version_sum = get_sum_versions(packet, 0)
    return version_sum

def evaluate(packet):
    version, packet_type, sub_packets = packet
    if packet_type == 0:
        return sum([evaluate(sub_packet) for sub_packet in sub_packets])
    elif packet_type == 1:
        prod = 1
        for n in (evaluate(sub_packet) for sub_packet in sub_packets):
            prod *= n
        return prod
    elif packet_type == 2:
        return min([evaluate(sub_packet) for sub_packet in sub_packets])
    elif packet_type == 3:
        return max([evaluate(sub_packet) for sub_packet in sub_packets])
    elif packet_type == 4:
        return sub_packets
    elif packet_type == 5:
        return 1 if evaluate(sub_packets[0]) > evaluate(sub_packets[1]) else 0
    elif packet_type == 6:
        return 1 if evaluate(sub_packets[0]) < evaluate(sub_packets[1]) else 0
    elif packet_type == 7:
        return 1 if evaluate(sub_packets[0]) == evaluate(sub_packets[1]) else 0

def solve_task2(lines):
    line = lines[0]
    binary = "".join([m[c] for c in line])
    line, packet = parse_packet(binary)
    return evaluate(packet)

if __name__ == '__main__':
    lines = read_lines('input.txt')
    # lines = read_lines('sample.txt')
    print('Task 1:', solve_task1(lines))
    print('Task 2:', solve_task2(lines))
