MOD = 1000000

def parse_fasta(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        rna_string = "".join(line.strip() for line in lines if not line.startswith(">"))
    return rna_string

def count_noncrossing_matchings(rna, memo={}):
    if rna in memo:
        return memo[rna]
    
    if len(rna) == 0:
        return 1  # Empty string has one way to match (trivial case)
    
    total_count = 0
    for i in range(1, len(rna), 2):
        # Check valid base pairing (A-U or C-G)
        if (rna[0] == 'A' and rna[i] == 'U') or \
           (rna[0] == 'U' and rna[i] == 'A') or \
           (rna[0] == 'C' and rna[i] == 'G') or \
           (rna[0] == 'G' and rna[i] == 'C'):
            
            # Recursively calculate for left and right subsequences
            left_count = count_noncrossing_matchings(rna[1:i], memo)
            right_count = count_noncrossing_matchings(rna[i+1:], memo)
            
            # Multiply the number of ways and add to total count
            total_count += left_count * right_count
            total_count %= MOD  # Apply modulo to keep number manageable
    
    memo[rna] = total_count
    return total_count

