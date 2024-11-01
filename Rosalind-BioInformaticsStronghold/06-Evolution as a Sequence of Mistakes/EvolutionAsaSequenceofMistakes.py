def hamming_distance(s, t):
    """Calculate the Hamming distance between two strings of equal length."""
    if len(s) != len(t):
        raise ValueError("Strings must be of equal length.")
    
    distance = 0
    for a, b in zip(s, t):
        if a != b:
            distance += 1
            
    return distance

def read_dna_from_file(file_path):
    """Read two DNA strings from a file and return them as a tuple."""
    with open(file_path, 'r') as file:
        # Read the two lines (strings) from the file
        s = file.readline().strip()
        t = file.readline().strip()
    return s, t
