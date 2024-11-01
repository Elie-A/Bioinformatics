from LongestIncreasingSubsequence import *

# Example usage
file_path = "Rosalind-BioInformaticsStronghold\\24-Longest Increasing Subsequence\\rosalind_lgis.txt"
n, permutation = read_input_file(file_path)
increasing, decreasing = find_longest_subsequences(n, permutation)

# Print results
print(" ".join(map(str, increasing)))
print(" ".join(map(str, decreasing)))
