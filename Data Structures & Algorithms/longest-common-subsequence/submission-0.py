class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # think about subproblem and recurrence
        # 1. subproblems: compare text1[1..i] and text2[2..j]
        # 2. recurrence: 
        # consider at last index i and j:
        # if text1[i] == text2[j]
        # count "+1" and take dp[i-1][j-1]

        # if text1[i] != text2[j]
        # -> dont count and take prev count dp[i][j-1] or dp[i-1][j]
        # intuition: skip char at j-1 or i-1
        i,j = len(text1), len(text2)
        dp = [[0] * (j+1) for _ in range(i+1)]

        dp[0][0] = 0
        for x in range(1,i+1):
            for y in range(1,j+1):
                if text1[x-1] == text2[y-1]:
                    dp[x][y] = 1 + dp[x-1][y-1]
                else:
                    dp[x][y] = max(dp[x-1][y], dp[x][y-1])

        return dp[i][j]