from CountingPhylogeneticAncestors import *

filename = 'Rosalind-BioInformaticsStronghold\\35-Counting Phylogenetic Ancestors\\rosalind_inod.txt'
n = read_data_from_file(filename)
print(count_internal_nodes(n))
