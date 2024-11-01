from itertools import permutations

def generate_permutations_from_file(filename):
    # Read n from the input file
    with open(filename, 'r') as file:
        n = int(file.readline().strip())
    
    # Generate all permutations of the list [1, 2, ..., n]
    nums = list(range(1, n + 1))
    all_permutations = list(permutations(nums))
    
    # Output the total number of permutations
    print(len(all_permutations))
    
    # Output each permutation in the required format
    for perm in all_permutations:
        print(" ".join(map(str, perm)))

