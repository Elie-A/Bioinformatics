from FindingASharedSplicedMotif import *

# Read the DNA strings from the file
filename = 'Rosalind-BioInformaticsStronghold\\38-Finding a Shared Spliced Motif\\rosalind_lcsq.txt'  # Replace with your actual file name
sequences = read_fasta(filename)
s, t = sequences[0], sequences[1]

# Find the longest common subsequence
lcs = longest_common_subsequence(s, t)
print(lcs)
