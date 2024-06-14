#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
# 相比v1去掉了sell中间变量


# 贪心算法
# 局部最优：每一步都选择当前最优解，希望通过这些局部最优解得到全局最优解。
# 寻找最小买入价格：在遍历的过程中，不断更新当前遇到的最小价格，这是为了保证我们能够以尽可能低的价格买入。
# 计算最大利润：同时检查当前价格减去之前的最小价格，是否能得到更高的利润，并将其与当前的最大利润进行比较，从而更新最大利润。
# 

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
                min_price = price # 更新最小买入价格
            elif price - min_price > max_profit:
                max_profit = price - min_price # 更新最大利润

        return max_profit
        
# @lc code=end

# from test import test
# test(Solution().maxProfit, [2,1,2,1,0,1,2])
# test(Solution().maxProfit, [2,4,1])
# test(Solution().maxProfit, [2,4,1,5])
# test(Solution().maxProfit, [7,1,5,3,6,4])
# test(Solution().maxProfit, [7,6,4,3,1])
