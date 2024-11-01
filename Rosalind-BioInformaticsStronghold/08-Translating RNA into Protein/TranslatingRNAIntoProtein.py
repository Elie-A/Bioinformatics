# Define the RNA codon table
CODON_TABLE = {
    'AUG': 'M', 'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 'AUU': 'I',
    'AUC': 'I', 'AUA': 'I', 'GUU': 'V', 'GUC': 'V', 'GUA': 'V',
    'GUG': 'V', 'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 'ACU': 'T',
    'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'GCU': 'A', 'GCC': 'A',
    'GCA': 'A', 'GCG': 'A', 'UAU': 'Y', 'UAC': 'Y', 'CAU': 'H',
    'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'AAU': 'N', 'AAC': 'N',
    'AAA': 'K', 'AAG': 'K', 'GAU': 'D', 'GAC': 'D', 'GAA': 'E',
    'GAG': 'E', 'UGU': 'C', 'UGC': 'C', 'UGG': 'W', 'CGU': 'R',
    'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGU': 'S', 'AGC': 'S',
    'AGA': 'R', 'AGG': 'R', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G',
    'GGG': 'G', 'UAA': '', 'UAG': '', 'UGA': ''  # Stop codons
}

def translate_rna_to_protein(rna_string):
    """Translate an RNA string into a protein string using the codon table."""
    protein_string = []
    
    # Process the RNA string in chunks of 3 bases (codons)
    for i in range(0, len(rna_string), 3):
        codon = rna_string[i:i+3]
        if codon in CODON_TABLE:
            amino_acid = CODON_TABLE[codon]
            if amino_acid:  # Stop translation if a stop codon is encountered
                protein_string.append(amino_acid)
            else:
                break  # Stop codon reached, end translation

    return ''.join(protein_string)

def read_rna_from_file(file_path):
    """Read the RNA sequence from a file."""
    with open(file_path, 'r') as file:
        rna_string = file.read().strip()
    return rna_string