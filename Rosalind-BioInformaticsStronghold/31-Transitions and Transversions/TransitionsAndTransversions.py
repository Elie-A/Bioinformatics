def parse_fasta(file_path):
    sequences = {}
    current_label = ""
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                current_label = line[1:]
                sequences[current_label] = ""
            else:
                sequences[current_label] += line
    return list(sequences.values())

def count_transitions_and_transversions(s1, s2):
    transitions = 0
    transversions = 0
    transition_pairs = {('A', 'G'), ('G', 'A'), ('C', 'T'), ('T', 'C')}
    
    for base1, base2 in zip(s1, s2):
        if base1 != base2:
            if (base1, base2) in transition_pairs:
                transitions += 1
            else:
                transversions += 1
    
    return transitions, transversions
