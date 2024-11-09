from CompletingATree import *

file_path = "Rosalind-BioInformaticsStronghold\\32-Completing a Tree\\rosalind_tree.txt"
n, edges = parse_input(file_path)

# Find the number of connected components
components = count_connected_components(n, edges)

# Calculate the minimum number of edges needed
edges_to_add = components - 1

# Output the result
print(edges_to_add)
