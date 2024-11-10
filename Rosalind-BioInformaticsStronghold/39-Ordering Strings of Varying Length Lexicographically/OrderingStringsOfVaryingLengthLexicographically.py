from itertools import product

def read_data_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
    alphabet = lines[0].split()
    n = int(lines[1])
    return alphabet, n

def generate_strings(alphabet, max_length):
    result = []
    for length in range(1, max_length + 1):
        for p in product(alphabet, repeat=length):
            result.append(''.join(p))
    return result