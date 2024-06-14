#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        buy, sell = 0, 1
        profit = max(0, prices[sell] - prices[buy])
        for i in range(1, len(prices)):
            if prices[i] < prices[buy]:
                buy = i
            elif prices[i] - prices[buy] > profit:
                sell = i
                profit = prices[sell] - prices[buy]
                # print('profit', buy, sell, profit)


        return profit
        
# @lc code=end

# from test import test
# test(Solution().maxProfit, [2,1,2,1,0,1,2])
# test(Solution().maxProfit, [2,4,1])
# test(Solution().maxProfit, [2,4,1,5])
# test(Solution().maxProfit, [7,1,5,3,6,4])
# test(Solution().maxProfit, [7,6,4,3,1])
