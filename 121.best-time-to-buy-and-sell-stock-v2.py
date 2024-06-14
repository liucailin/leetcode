#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
# 去掉了sell中间变量

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
        
# @lc code=end

# from test import test
# test(Solution().maxProfit, [2,1,2,1,0,1,2])
# test(Solution().maxProfit, [2,4,1])
# test(Solution().maxProfit, [2,4,1,5])
# test(Solution().maxProfit, [7,1,5,3,6,4])
# test(Solution().maxProfit, [7,6,4,3,1])
