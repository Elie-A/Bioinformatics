from TransitionsAndTransversions import *

# Read data from file
file_path = "Rosalind-BioInformaticsStronghold\\31-Transitions and Transversions\\rosalind_tran.txt"
s1, s2 = parse_fasta(file_path)

# Count transitions and transversions
transitions, transversions = count_transitions_and_transversions(s1, s2)

# Calculate the ratio
if transversions == 0:
    ratio = float('inf')  # Handle case of zero transversions
else:
    ratio = transitions / transversions

# Output the result
print(f"{ratio:.11f}")
