from ConsensusAndProfile import *
# Specify the path to the input file in FASTA format
file_path = "Rosalind-BioInformaticsStronghold\\10-Consensus and Profile\\rosalind_cons.txt"  

# Parse the FASTA file and extract DNA strings
dna_strings = parse_fasta(file_path)

# Build the profile matrix and get the consensus string
consensus, profile = build_profile_matrix(dna_strings)

# Output the results
print_profile_matrix(consensus, profile)
