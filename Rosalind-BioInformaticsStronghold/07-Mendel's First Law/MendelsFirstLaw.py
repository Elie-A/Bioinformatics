def dominant_phenotype_probability(k, m, n):
    """Calculate the probability of producing offspring with a dominant phenotype."""
    total_population = k + m + n
    total_pairs = total_population * (total_population - 1)
    
    # Probabilities for each pairing outcome
    prob_kk = (k / total_population) * ((k - 1) / (total_population - 1))
    prob_km = 2 * (k / total_population) * (m / (total_population - 1))
    prob_kn = 2 * (k / total_population) * (n / (total_population - 1))
    prob_mm = (m / total_population) * ((m - 1) / (total_population - 1)) * 0.75
    prob_mn = 2 * (m / total_population) * (n / (total_population - 1)) * 0.5
    prob_nn = (n / total_population) * ((n - 1) / (total_population - 1)) * 0
    
    dominant_probability = prob_kk + prob_km + prob_kn + prob_mm + prob_mn + prob_nn
    return dominant_probability

def read_dataset_from_file(file_path):
    """Read the integers k, m, and n from a file."""
    with open(file_path, 'r') as file:
        data = file.readline().strip()
        k, m, n = map(int, data.split())
    return k, m, n
