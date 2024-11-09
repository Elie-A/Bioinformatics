def parse_fasta_from_file(filename):
    reads = {}
    with open(filename, 'r') as file:
        current_label = ""
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                current_label = line[1:]
                reads[current_label] = ""
            else:
                reads[current_label] += line
    return list(reads.values())

def hamming_distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

def reverse_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return "".join(complement[base] for base in reversed(dna))

def find_corrections(reads):
    correct_reads = set()
    read_counts = {}
    
    for read in reads:
        read_counts[read] = read_counts.get(read, 0) + 1
        rev_comp = reverse_complement(read)
        read_counts[rev_comp] = read_counts.get(rev_comp, 0) + 1
    
    for read, count in read_counts.items():
        if count > 1:
            correct_reads.add(read)
    
    corrections = []
    
    for read in reads:
        if read not in correct_reads:
            for correct_read in correct_reads:
                if hamming_distance(read, correct_read) == 1:
                    corrections.append(f"{read}->{correct_read}")
                    break
    
    return corrections