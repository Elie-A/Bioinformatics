def reverse_complement(dna_string):
    # Create a complement mapping
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    
    # Reverse the DNA string and get the complement
    reverse_comp = ''.join(complement[nucleotide] for nucleotide in reversed(dna_string))
    
    return reverse_comp