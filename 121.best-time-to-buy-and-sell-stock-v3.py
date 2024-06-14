#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock


# 动态规划
# 在这类问题中，可以使用两个数组来存储相关状态：
# dp[i][0]：表示到第 i 天为止，手上不持有股票的最大利润。
# dp[i][1]：表示到第 i 天为止，手上持有股票的最大利润。
# 状态转移方程
# 对于 dp[i][0]：
# 如果今天手上不持有股票，那么有两种可能：
# 今天没有任何操作，即继承昨天的状态，dp[i][0] = dp[i-1][0]
# 今天卖出股票，那么昨天必须持有股票，dp[i][0] = dp[i-1][1] + prices[i]
# 因此，dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
# 对于 dp[i][1]：
# 如果今天手上持有股票，那么有两种可能：
# 今天没有任何操作，即继承昨天的状态，dp[i][1] = dp[i-1][1]
# 今天买入股票，那么昨天必须不持有股票，dp[i][1] = -prices[i] 因为这是第一次交易，或者我们可以考虑在以前买进的状态。
# 因此，dp[i][1] = max(dp[i-1][1], -prices[i])（因为最多只允许进行一次交易，因此直接买入）
# 初始条件
# dp[0][0] = 0，因为第一天没有股票，利润为0。
# dp[0][1] = -prices[0]，第一天买入股票的利润记为负数，因为是支出。

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        dp = [[0]*2 for _ in range(n)]

        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], prices[i] + dp[i-1][1])
            dp[i][1] = max(dp[i-1][1], -prices[i])

        return dp[n-1][0]
        
# @lc code=end

# from test import test
# test(Solution().maxProfit, [2,1,2,1,0,1,2])
# test(Solution().maxProfit, [2,4,1])
# test(Solution().maxProfit, [2,4,1,5])
# test(Solution().maxProfit, [7,1,5,3,6,4])
# test(Solution().maxProfit, [7,6,4,3,1])
