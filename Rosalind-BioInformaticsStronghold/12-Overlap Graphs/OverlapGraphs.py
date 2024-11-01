def parse_fasta(file_path):
    """Parses a FASTA file and returns a dictionary of sequences with their IDs."""
    sequences = {}
    with open(file_path, "r") as file:
        sequence_id = None
        sequence_data = []
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if sequence_id:
                    sequences[sequence_id] = ''.join(sequence_data)
                sequence_id = line[1:]
                sequence_data = []
            else:
                sequence_data.append(line)
        if sequence_id:
            sequences[sequence_id] = ''.join(sequence_data)
    return sequences

def build_overlap_graph(sequences, k=3):
    """Builds an overlap graph with edges based on matching suffix/prefix of length k."""
    adjacency_list = []
    for id1, seq1 in sequences.items():
        suffix = seq1[-k:]
        for id2, seq2 in sequences.items():
            if id1 != id2 and seq2.startswith(suffix):
                adjacency_list.append((id1, id2))
    return adjacency_list