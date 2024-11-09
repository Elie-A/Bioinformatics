from KMerComposition import *

# Read the DNA string from the file
filename = 'Rosalind-BioInformaticsStronghold\\36-k-Mer Composition\\rosalind_kmer.txt' 
sequence = read_fasta(filename)

# Calculate the 4-mer composition
k = 4
composition = kmer_composition(sequence, k)

# Print the 4-mer composition
print(' '.join(map(str, composition)))
