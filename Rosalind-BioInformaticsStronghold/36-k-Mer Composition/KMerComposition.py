from itertools import product

def read_fasta(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    sequence = ''.join(line.strip() for line in lines if not line.startswith('>'))
    return sequence

def generate_kmers(k):
    return [''.join(kmer) for kmer in product('ACGT', repeat=k)]

def kmer_composition(s, k):
    kmers = generate_kmers(k)
    kmer_count = {kmer: 0 for kmer in kmers}
    
    for i in range(len(s) - k + 1):
        kmer = s[i:i+k]
        if kmer in kmer_count:
            kmer_count[kmer] += 1
    
    return [kmer_count[kmer] for kmer in kmers]

