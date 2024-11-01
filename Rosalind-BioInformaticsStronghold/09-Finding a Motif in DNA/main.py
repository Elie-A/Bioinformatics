from FindingaMotifInDNA import *

# Specify the file path where the dataset is stored
file_path = "Rosalind-BioInformaticsStronghold\\09-Finding a Motif in DNA\\rosalind_subs.txt"

# Read data from file
s, t = read_data_from_file(file_path)

# Find and print all starting positions of t in s
positions = find_substring_locations(s, t)
print(" ".join(map(str, positions)))
