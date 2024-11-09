from Bio import SeqIO

def find_overlap(s1, s2, min_overlap):
    """
    Returns the length of the maximum suffix of s1 that matches a prefix of s2
    and is at least `min_overlap` characters long.
    """
    start = 0  # Start looking from the beginning of s1
    while True:
        start = s1.find(s2[:min_overlap], start)  # Find s2's prefix in s1
        if start == -1:  # No more occurrences found
            return 0
        # Check if the suffix of s1 matches the prefix of s2
        if s1[start:] == s2[:len(s1) - start]:
            return len(s1) - start
        start += 1

def shortest_superstring(reads):
    """
    Constructs the shortest superstring containing all reads.
    """
    min_overlap = len(reads[0]) // 2  # Minimum overlap is half the read length

    while len(reads) > 1:
        max_len, i, j = -1, 0, 0
        # Find the pair with maximum overlap
        for x in range(len(reads)):
            for y in range(len(reads)):
                if x != y:
                    overlap_len = find_overlap(reads[x], reads[y], min_overlap)
                    if overlap_len > max_len:
                        max_len, i, j = overlap_len, x, y

        # Merge reads[i] and reads[j] with max overlap
        reads[i] = reads[i] + reads[j][max_len:]
        del reads[j]

    return reads[0]

