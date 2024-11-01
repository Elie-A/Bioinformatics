from Bio.Seq import Seq
from Bio import SeqIO

def dna_to_protein(fasta_file):
    # Parse the input FASTA file
    sequences = list(SeqIO.parse(fasta_file, "fasta"))
    
    # The first sequence is the main DNA string, others are introns
    dna_sequence = str(sequences[0].seq)
    introns = [str(seq.seq) for seq in sequences[1:]]

    # Remove introns from the DNA sequence
    for intron in introns:
        dna_sequence = dna_sequence.replace(intron, "")

    # Convert remaining DNA to mRNA by replacing T with U
    mrna_sequence = dna_sequence.replace("T", "U")

    # Translate mRNA to protein
    protein_sequence = str(Seq(mrna_sequence).translate(to_stop=True))
    
    return protein_sequence