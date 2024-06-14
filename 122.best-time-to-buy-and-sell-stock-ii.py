#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0

        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]

        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], prices[i] + dp[i-1][1])
            dp[i][1] = max(dp[i-1][1], -prices[i] + dp[i-1][0])

        
        return dp[n-1][0]

        
# @lc code=end


# from test import test
# test(Solution().maxProfit, [7,1,5,3,6,4])
# test(Solution().maxProfit, [1,2,3,4,5])
# test(Solution().maxProfit, [7,6,4,3,1])
