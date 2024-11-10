from SpeedingUpMotifFinding import *

# Read the DNA string from the file
filename = 'Rosalind-BioInformaticsStronghold\\37-Speeding Up Motif Finding\\rosalind_kmp.txt'
sequence = read_fasta(filename)

# Compute the failure array
failure_array = compute_failure_array(sequence)

# Print the failure array
print(' '.join(map(str, failure_array)))
