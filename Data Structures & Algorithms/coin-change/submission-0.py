class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [float("inf")] * (amount+1)
        dp[0] = 0

        # dp[i] is the number of coins to have amount i
        # we want the least number --> use min
        for i in range(1,amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i - coin]+1, dp[i])

        return dp[amount] if dp[amount] != float("inf") else -1