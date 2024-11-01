from CountingDNANucleotides import *

with open("Rosalind-BioInformaticsStronghold\\01-Counting DNA Nucleotides\\rosalind_dna.txt", "r") as file:
    dna_string = file.read().strip()

result = countNucleotidesFrequency(dna_string)
print(' '.join([str(val) for key, val in result.items()]))
