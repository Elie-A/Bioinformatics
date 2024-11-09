from Bio import SeqIO
import math
import sys

def count_perfect_matchings(rna):
    # Count occurrences of each nucleotide
    num_A = rna.count('A')
    num_U = rna.count('U')
    num_C = rna.count('C')
    num_G = rna.count('G')
    
    # Ensure equal numbers for A-U and C-G pairs
    if num_A != num_U or num_C != num_G:
        return 0  # No perfect matching possible if not equal
    
    # Calculate perfect matchings as factorial of A and C counts
    matchings_AU = math.factorial(num_A)
    matchings_CG = math.factorial(num_C)
    
    return matchings_AU * matchings_CG

# Reading the RNA sequence from a FASTA file
def read_rna_from_fasta(file_path):
    try:
        record = next(SeqIO.parse(file_path, "fasta"))
        rna_sequence = str(record.seq)
        if not all(base in "AUCG" for base in rna_sequence):
            raise ValueError("The sequence contains invalid characters. Ensure it only has A, U, C, and G.")
        return rna_sequence
    except FileNotFoundError:
        sys.exit("File not found. Please check the file path.")
    except StopIteration:
        sys.exit("The FASTA file is empty or improperly formatted.")
    except Exception as e:
        sys.exit(f"An error occurred: {e}")