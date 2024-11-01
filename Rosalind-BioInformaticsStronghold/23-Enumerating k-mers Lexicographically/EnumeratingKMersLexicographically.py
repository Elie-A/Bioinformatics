from itertools import product

def generate_lexicographic_strings(file_path):
    # Read the file content
    with open(file_path, 'r') as file:
        # Read the first line as the alphabet, split by spaces
        alphabet = file.readline().strip().split()
        # Read the second line as an integer n
        n = int(file.readline().strip())
    
    # Generate all combinations of length n from the alphabet
    combinations = product(alphabet, repeat=n)
    
    # Join tuples into strings and collect them
    result = ["".join(comb) for comb in combinations]
    
    # Print each string in a new line
    for s in result:
        print(s)

