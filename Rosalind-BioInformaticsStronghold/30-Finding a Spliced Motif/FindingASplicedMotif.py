def parse_fasta(file_path):
    sequences = {}
    current_label = ""
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                current_label = line[1:]  # Remove '>'
                sequences[current_label] = ""
            else:
                sequences[current_label] += line
    return list(sequences.values())

def find_subsequence_indices(s, t):
    indices = []
    t_index = 0
    for i, char in enumerate(s):
        if char == t[t_index]:
            indices.append(i + 1)  # 1-based index
            t_index += 1
            if t_index == len(t):  # We found the entire subsequence
                break
    return indices