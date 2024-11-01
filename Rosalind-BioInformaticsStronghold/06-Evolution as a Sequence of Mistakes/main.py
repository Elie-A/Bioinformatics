from EvolutionAsaSequenceofMistakes import *

# Specify the path to your input file
file_path = "Rosalind-BioInformaticsStronghold\\06-Evolution as a Sequence of Mistakes\\rosalind_hamm.txt"

# Read the DNA strings from the file
s, t = read_dna_from_file(file_path)

# Calculate and print the Hamming distance
result = hamming_distance(s, t)
print(result)  # Output will be the Hamming distance
