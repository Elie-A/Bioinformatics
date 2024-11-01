from Bio import SeqIO

def longest_common_substring(strings):
    # Sort strings by length to start with the shortest one
    shortest_str = min(strings, key=len)
    
    # Iterate over all substrings of the shortest string in descending order of length
    for length in range(len(shortest_str), 0, -1):
        for start in range(len(shortest_str) - length + 1):
            candidate = shortest_str[start:start + length]
            
            # Check if candidate is in all other strings
            if all(candidate in s for s in strings):
                return candidate
    return ""
