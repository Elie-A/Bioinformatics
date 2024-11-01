def edit_distance(s1, s2):
    """Calculate the edit distance between two strings using dynamic programming."""
    len_s1, len_s2 = len(s1), len(s2)
    dp = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]
    
    # Initialize base cases
    for i in range(len_s1 + 1):
        dp[i][0] = i  # Deletion
    for j in range(len_s2 + 1):
        dp[0][j] = j  # Insertion

    # Fill the DP table
    for i in range(1, len_s1 + 1):
        for j in range(1, len_s2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No operation needed
            else:
                dp[i][j] = min(dp[i - 1][j] + 1,   # Deletion
                               dp[i][j - 1] + 1,   # Insertion
                               dp[i - 1][j - 1] + 1)  # Substitution

    return dp[len_s1][len_s2]

def find_motif_locations(k, motif, genome):
    motif_length = len(motif)
    results = []

    # Check all substrings of genome with the same length as the motif
    for start in range(len(genome) - motif_length + 1):
        substring = genome[start:start + motif_length]
        distance = edit_distance(motif, substring)
        
        if distance <= k:
            results.append((start + 1, motif_length))  # +1 for 1-based indexing
    
    return results