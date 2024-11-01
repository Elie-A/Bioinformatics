from ComputingGCContent import *

# Usage
file_path = "Rosalind-BioInformaticsStronghold\\05-Computing GC Content\\rosalind_gc.txt"  
fasta_dict = parse_fasta(file_path)
highest_gc_id, highest_gc_content = find_highest_gc_content(fasta_dict)

# Output the result
print(highest_gc_id)
print(f"{highest_gc_content:.6f}")  # Format to 6 decimal places
