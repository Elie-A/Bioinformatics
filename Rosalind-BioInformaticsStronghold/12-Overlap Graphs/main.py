from OverlapGraphs import *

def main():
    # Parse the sequences from a FASTA file
    sequences = parse_fasta("Rosalind-BioInformaticsStronghold\\12-Overlap Graphs\\rosalind_grph.txt")
    
    # Build the overlap graph
    adjacency_list = build_overlap_graph(sequences, k=3)
    
    # Print the adjacency list
    for edge in adjacency_list:
        print(f"{edge[0]} {edge[1]}")

# Run the main function
main()
