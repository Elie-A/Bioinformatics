from InferringmRNAFromProtein import *

# Main execution
filename = 'Rosalind-BioInformaticsStronghold\\17-Inferring mRNA from Protein\\rosalind_mrna.txt'
protein_string = read_protein_from_file(filename)
output = count_rna_strings_with_stop_codon(protein_string)
print(output)
