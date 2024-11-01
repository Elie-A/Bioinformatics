def rabbit_pairs(n, k):
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 1
    
    for month in range(3, n + 1):
        dp[month] = dp[month - 1] + k * dp[month - 2]
    
    return dp[n]