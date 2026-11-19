class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 1. subproblems:
        # count the # of edit in word1[1..i] and word2[1..j]
        
        # 2. recurrence:
        # 2 states: match or unmatch
        # if match (word1[i] == word2[j])
        # dp[i][j] = dp[i-1][j-1] -> skip character at i and j

        # if unmatch (word1[i] != word2[j])
        # 2.1 insert
        # dp[i][j] = 1 + dp[i][j-1]
        # 2.2 delete
        # dp[i][j] = 1 + dp[i-1][j]
        # 2.3 replace
        # dp[i][j] = 1 + dp[i-1][j-1]

        m,n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            dp[i][0] = i
        for j in range(1, n+1):
            dp[0][j] = j

        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        return dp[m][n]





