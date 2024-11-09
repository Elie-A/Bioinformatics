def count_internal_nodes(n): return n - 2

def count_internal_nodes(n):
    return n - 2

# Read data from file
def read_data_from_file(filename):
    with open(filename, 'r') as file:
        n = int(file.read().strip())
    return n