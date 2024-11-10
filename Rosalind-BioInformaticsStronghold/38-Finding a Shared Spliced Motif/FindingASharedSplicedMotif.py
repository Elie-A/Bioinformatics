def read_fasta(filename):
    sequences = {}
    with open(filename, 'r') as file:
        current_label = ""
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                current_label = line[1:]
                sequences[current_label] = ""
            else:
                sequences[current_label] += line
    return list(sequences.values())

def longest_common_subsequence(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs = []
    while m > 0 and n > 0:
        if s[m - 1] == t[n - 1]:
            lcs.append(s[m - 1])
            m -= 1
            n -= 1
        elif dp[m - 1][n] > dp[m][n - 1]:
            m -= 1
        else:
            n -= 1

    return ''.join(reversed(lcs))