from Bio.Seq import Seq
from Bio import SeqIO

# Constants
START_CODON = "ATG"
STOP_CODONS = {"TAA", "TAG", "TGA"}

def get_orfs(dna_sequence):
    """Find all open reading frames in all six reading frames of a DNA sequence."""
    orfs = set()

    def find_orfs_in_frame(seq):
        """Finds all candidate proteins in one reading frame."""
        n = len(seq)
        i = 0
        while i < n - 2:
            # Look for the start codon
            if seq[i:i+3] == START_CODON:
                protein = []
                has_stop = False
                for j in range(i, n - 2, 3):
                    codon = seq[j:j+3]
                    if codon in STOP_CODONS:
                        has_stop = True
                        break
                    protein.append(codon)
                # If valid ORF, translate and add to set
                if has_stop:
                    protein_seq = str(Seq("".join(protein)).translate())
                    orfs.add(protein_seq)
            i += 1

    # Check all frames for the original DNA sequence
    for frame in range(3):
        find_orfs_in_frame(dna_sequence[frame:])
    
    # Check all frames for the reverse complement
    reverse_complement = str(Seq(dna_sequence).reverse_complement())
    for frame in range(3):
        find_orfs_in_frame(reverse_complement[frame:])
    
    return orfs

def read_fasta(filename):
    for record in SeqIO.parse(filename, "fasta"):
        return str(record.seq)

def find_candidate_proteins(filename):
    dna_sequence = read_fasta(filename)
    proteins = get_orfs(dna_sequence)
    # Print each unique protein sequence with a newline after each
    for protein in proteins:
        print(protein)
    print()  # Ensure final newline
