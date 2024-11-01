from ComplementingAStrandOfDNA import *

with open("Rosalind-BioInformaticsStronghold\\03-Complementing a Strand of DNA\\rosalind_revc.txt", "r") as file:
    dna_string = file.read().strip()

print(reverse_complement(dna_string))