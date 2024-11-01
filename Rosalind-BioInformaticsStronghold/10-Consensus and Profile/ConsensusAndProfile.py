from collections import defaultdict

def parse_fasta(file_path):
    """Parse FASTA file and return a list of DNA strings."""
    sequences = []
    with open(file_path, 'r') as file:
        sequence = ""
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if sequence:
                    sequences.append(sequence)
                sequence = ""
            else:
                sequence += line
        if sequence:
            sequences.append(sequence)
    return sequences

def build_profile_matrix(dna_strings):
    """Build profile matrix and consensus string from DNA strings."""
    length = len(dna_strings[0])
    profile = defaultdict(lambda: [0] * length)
    
    # Populate the profile matrix
    for dna in dna_strings:
        for i, nucleotide in enumerate(dna):
            profile[nucleotide][i] += 1

    # Build the consensus string
    consensus = ""
    for i in range(length):
        max_count = 0
        max_nucleotide = ""
        for nucleotide in "ACGT":
            if profile[nucleotide][i] > max_count:
                max_count = profile[nucleotide][i]
                max_nucleotide = nucleotide
        consensus += max_nucleotide
    
    return consensus, profile

def print_profile_matrix(consensus, profile):
    """Print the consensus string and profile matrix in the required format."""
    print(consensus)
    for nucleotide in "ACGT":
        print(f"{nucleotide}: {' '.join(map(str, profile[nucleotide]))}")