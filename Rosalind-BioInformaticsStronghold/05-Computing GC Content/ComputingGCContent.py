def calculate_gc_content(dna_string):
    """Calculate the GC-content percentage of a DNA string."""
    g_count = dna_string.count('G')
    c_count = dna_string.count('C')
    total_count = len(dna_string)
    if total_count == 0:  # Prevent division by zero
        return 0
    return (g_count + c_count) / total_count * 100

def parse_fasta(file_path):
    """Parse the FASTA formatted file and return a dictionary of IDs and sequences."""
    with open(file_path, 'r') as file:
        fasta_dict = {}
        current_id = ""
        current_sequence = ""

        for line in file:
            line = line.strip()
            if line.startswith(">"):
                # If we have a current sequence, save it before moving to the next ID
                if current_id:
                    fasta_dict[current_id] = current_sequence
                current_id = line[1:]  # Get the ID without '>'
                current_sequence = ""  # Reset current sequence
            else:
                current_sequence += line  # Append sequence lines
        
        # Don't forget to add the last entry
        if current_id:
            fasta_dict[current_id] = current_sequence

    return fasta_dict

def find_highest_gc_content(fasta_dict):
    """Find the ID with the highest GC-content and return it along with the GC-content value."""
    max_gc_content = 0
    max_id = ""
    
    for identifier, sequence in fasta_dict.items():
        gc_content = calculate_gc_content(sequence)
        if gc_content > max_gc_content:
            max_gc_content = gc_content
            max_id = identifier
    
    return max_id, max_gc_content