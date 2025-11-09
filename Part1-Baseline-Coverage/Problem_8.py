"""
Problem 8 - From CodeScore-MBPP-ET:
Write a function to find the minimum cost path to reach (m, n) from (0, 0) for the given cost matrix cost[][] 
and a position (m, n) in cost[][].

"""

def solution1(cost, m, n):
    if not cost or not cost[0]:
        raise ValueError("cost matrix must be non-empty")
    rows = len(cost)
    cols = len(cost[0])
    if not (0 <= m < rows and 0 <= n < cols):
        raise ValueError("target (m,n) out of bounds")

    dp = [[0] * cols for _ in range(rows)]
    dp[0][0] = cost[0][0]

    # first row
    for j in range(1, cols):
        dp[0][j] = dp[0][j-1] + cost[0][j]
    # first column
    for i in range(1, rows):
        dp[i][0] = dp[i-1][0] + cost[i][0]

    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = cost[i][j] + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

    return dp[m][n]