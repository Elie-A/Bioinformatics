from IndependentAlleles import *

file_path = 'Rosalind-BioInformaticsStronghold\\15-Independent Alleles\\rosalind_lia.txt'
k, N = read_data_from_file(file_path)
output = probability_AaBb(k, N)
print(output)  # This will print the calculated probability
