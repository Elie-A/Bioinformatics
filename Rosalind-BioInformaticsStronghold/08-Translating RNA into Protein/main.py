from TranslatingRNAIntoProtein import *

# Specify the path to your input file
file_path = "Rosalind-BioInformaticsStronghold\\08-Translating RNA into Protein\\rosalind_prot.txt"

# Read the RNA sequence from the file
rna_string = read_rna_from_file(file_path)

# Translate and print the protein string
protein_string = translate_rna_to_protein(rna_string)
print(protein_string)
