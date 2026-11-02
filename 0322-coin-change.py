# 322. Coin Change (Medium)
# https://leetcode.com/problems/coin-change/
# Approach: bottom-up DP; dp[x] = fewest coins to make amount x.
# Time: O(amount * len(coins))  Space: O(amount)
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float("inf")] * amount
        for x in range(1, amount + 1):
            for c in coins:
                if c <= x:
                    dp[x] = min(dp[x], dp[x - c] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1
