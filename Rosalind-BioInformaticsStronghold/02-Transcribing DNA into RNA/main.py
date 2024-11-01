from TranscribeDNAIntoRNA import *

with open("Rosalind-BioInformaticsStronghold\\02-Transcribing DNA into RNA\\rosalind_rna.txt", "r") as file:
    dna_string = file.read().strip()

rna = transcribe_dna_to_rna(dna_string)
print(rna)
