from itertools import permutations, product

def signed_permutations(n):
    numbers = range(1, n + 1)
    unsigned_permutations = list(permutations(numbers))
    sign_combinations = list(product([-1, 1], repeat=n))
    
    signed_permutations_list = []
    
    for perm in unsigned_permutations:
        for signs in sign_combinations:
            signed_perm = [a * b for a, b in zip(perm, signs)]
            signed_permutations_list.append(signed_perm)
    
    return len(signed_permutations_list), signed_permutations_list