from MendelsFirstLaw import *

# Specify the path to your input file
file_path = "Rosalind-BioInformaticsStronghold\\07-Mendel's First Law\\rosalind_iprb.txt"

# Read the values of k, m, and n from the file
k, m, n = read_dataset_from_file(file_path)

# Calculate and print the probability
result = dominant_phenotype_probability(k, m, n)
print(f"{result:.5f}")