def isValidPalindrome(s: str, k: int) -> bool:
    def longestPalindromeSubseq(s: str) -> int:
        return longestCommonSubsequence(s, s[::-1])

    def longestCommonSubsequence(text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0]*(m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                    
        return dp[n][m]

    return longestPalindromeSubseq(s) + k >= len(s)
