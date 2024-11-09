from FindingASplicedMotif import *

file_path = "Rosalind-BioInformaticsStronghold\\30-Finding a Spliced Motif\\rosalind_sseq.txt"
s, t = parse_fasta(file_path)

# Find indices of subsequence
indices = find_subsequence_indices(s, t)

# Output result
print(" ".join(map(str, indices)))
