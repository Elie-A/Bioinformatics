from Bio import SeqIO
from Bio.Seq import Seq

def find_reverse_palindromes(dna_sequence):
    palindromic_sites = []
    sequence_length = len(dna_sequence)
    
    # Loop over each possible starting position
    for i in range(sequence_length):
        # Check substrings of lengths from 4 to 12
        for length in range(4, 13):
            # Ensure the substring doesn't exceed the sequence bounds
            if i + length > sequence_length:
                break
            
            # Get the substring and its reverse complement
            substring = dna_sequence[i:i+length]
            reverse_complement = str(Seq(substring).reverse_complement())
            
            # Check if the substring is a reverse palindrome
            if substring == reverse_complement:
                # Record the starting position (1-based) and length
                palindromic_sites.append((i + 1, length))
    
    return palindromic_sites

# Read DNA sequence in FASTA format
def read_fasta(filename):
    for record in SeqIO.parse(filename, "fasta"):
        return str(record.seq)

# Main function to find palindromic sites from file input
def find_palindromic_sites_from_file(filename):
    dna_sequence = read_fasta(filename)
    palindromic_sites = find_reverse_palindromes(dna_sequence)
    
    # Print each palindromic site in the required format
    for position, length in palindromic_sites:
        print(position, length)

