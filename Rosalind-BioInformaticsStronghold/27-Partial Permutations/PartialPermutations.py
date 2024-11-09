def partial_permutations(n, k, mod=1000000):
    result = 1
    for i in range(k):
        result = (result * (n - i)) % mod
    return result

# Function to read data from file and calculate partial permutations
def read_data_and_calculate(file_path):
    with open(file_path, 'r') as file:
        # Read the line and split it to get n and k
        line = file.readline().strip()
        n, k = map(int, line.split())
        
    # Calculate partial permutations with the read values
    return partial_permutations(n, k)