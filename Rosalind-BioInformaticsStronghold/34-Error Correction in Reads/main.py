from ErrorCorrectionInReads import *

# Read data from file and output corrections
filename = 'Rosalind-BioInformaticsStronghold\\34-Error Correction in Reads\\rosalind_corr.txt'
reads = parse_fasta_from_file(filename)
corrections = find_corrections(reads)
for correction in corrections:
    print(correction)
