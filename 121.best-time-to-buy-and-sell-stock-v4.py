#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock


# 动态规划
# 优化空间存储，由于 dp[i][0] 和 dp[i][1] 只与前一天的状态有关，
# 我们可以优化空间复杂度，将 dp 数组压缩为两个变量而不是使用二维数组：

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        dp0 = 0
        dp1 = -prices[0]

        for i in range(1, n):
            dp0 = max(dp0, prices[i] + dp1)
            dp1 = max(dp1, -prices[i])

        return dp0

        
# @lc code=end

# from test import test
# test(Solution().maxProfit, [2,1,2,1,0,1,2])
# test(Solution().maxProfit, [2,4,1])
# test(Solution().maxProfit, [2,4,1,5])
# test(Solution().maxProfit, [7,1,5,3,6,4])
# test(Solution().maxProfit, [7,6,4,3,1])
