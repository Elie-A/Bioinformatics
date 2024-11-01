from math import comb

def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        line = file.readline().strip()
        k, N = map(int, line.split())
    return k, N

def probability_AaBb(k, N):
    # Total number of organisms in k-th generation
    m = 2 ** k  # Each generation doubles the number of organisms
    p = 0.25  # Probability of an AaBb offspring

    # Probability of having at least N AaBb offspring
    probability_at_least_N = 0.0
    
    # Calculate the probability of having less than N AaBb organisms
    for x in range(N):
        probability_x = comb(m, x) * (p ** x) * ((1 - p) ** (m - x))
        probability_at_least_N += probability_x
    
    # P(X >= N) = 1 - P(X < N)
    probability_at_least_N = 1 - probability_at_least_N
    return round(probability_at_least_N, 3)

