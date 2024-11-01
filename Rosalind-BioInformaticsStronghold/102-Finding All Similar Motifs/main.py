from FindingAllSimilarMotifs import *

# Sample Dataset
k = 2
motif = "ACGTAG"
genome = "ACGGATCGGCATCGT"

# Find locations and print results
results = find_motif_locations(k, motif, genome)
for location in results:
    print(location[0], location[1])  # Output: position and length
