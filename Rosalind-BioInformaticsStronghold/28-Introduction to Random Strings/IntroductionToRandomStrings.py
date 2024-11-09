import math

def log_probability(s, gc_content):
    # Probability for GC and AT based on the GC content
    prob_gc = math.log10(gc_content / 2)
    prob_at = math.log10((1 - gc_content) / 2)
    
    # Calculate the log probability for the string s
    log_prob = 0
    for base in s:
        if base in "GC":
            log_prob += prob_gc
        elif base in "AT":
            log_prob += prob_at
    return log_prob

def calculate_log_probabilities(s, gc_contents):
    # Calculate log probabilities for each GC content in the list
    return [log_probability(s, gc) for gc in gc_contents]

def read_data_and_calculate(file_path):
    # Read data from file
    with open(file_path, 'r') as file:
        # First line is the DNA string
        s = file.readline().strip()
        # Second line contains GC-content values as a space-separated string
        gc_contents = list(map(float, file.readline().strip().split()))
    
    # Calculate log probabilities for each GC-content
    return calculate_log_probabilities(s, gc_contents)