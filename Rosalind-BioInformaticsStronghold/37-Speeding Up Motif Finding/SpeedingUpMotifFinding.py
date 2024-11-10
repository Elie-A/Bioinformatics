def read_fasta(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    sequence = ''.join(line.strip() for line in lines if not line.startswith('>'))
    return sequence

def compute_failure_array(s):
    n = len(s)
    P = [0] * n
    k = 0
    for i in range(1, n):
        while k > 0 and s[k] != s[i]:
            k = P[k - 1]
        if s[k] == s[i]:
            k += 1
        P[i] = k
    return P
