from PerfectMatchingsAndRNASecondaryStructures import *

file_path = "Rosalind-BioInformaticsStronghold\\26-Perfect Matchings and RNA Secondary Structures\\rosalind_pmch.txt"
rna_sequence = read_rna_from_fasta(file_path)
result = count_perfect_matchings(rna_sequence)
print(result)
