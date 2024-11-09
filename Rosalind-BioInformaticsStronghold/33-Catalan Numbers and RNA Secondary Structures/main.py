from CatalanNumbersAndRNASecondaryStructures import *

# Read RNA string from file
file_path = "Rosalind-BioInformaticsStronghold\\33-Catalan Numbers and RNA Secondary Structures\\rosalind_cat.txt"
rna_string = parse_fasta(file_path)

# Calculate and print the result
result = count_noncrossing_matchings(rna_string)
print(result)
