import sys

if __name__ == "__main__":
    first = sys.stdin.readline().split()
    second = sys.stdin.readline().split()
    
    N = len(first)
    M = len(second)
    dp = [[0 for i in range(M + 1)] for j in range(N + 1)]
    

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if first[i - 1] == second[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    print(dp[N][M])