from GenomeAssemblyAsShortestSuperstring import *

# Read the sequences from FASTA format
sequences = []
with open("Rosalind-BioInformaticsStronghold\\25-Genome Assembly as Shortest Superstring\\rosalind_long.txt") as fasta_file:
    for record in SeqIO.parse(fasta_file, "fasta"):
        sequences.append(str(record.seq))

# Get the shortest superstring
result = shortest_superstring(sequences)
print(result)
