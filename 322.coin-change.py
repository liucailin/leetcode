#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#


def coinChange_Brute(coins, amount):
    """
    暴力解决
    写出递归式
    """
    if amount == 0:
        return 0
    if amount < 0:
        return -1
    min_count = float('inf')
    for coin in coins:
        count = coinChange_Brute(coins, amount - coin)
        if count == -1:
            continue
        min_count = min(count + 1, min_count)
    return -1 if min_count == float('inf') else min_count

    


# @lc code=start
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [float('inf')] * (amount + 1)

        dp[0] = 0
        for coin in coins:
            for i in range(len(dp)):
                if i < coin:
                    continue
                dp[i] = min(dp[i - coin] + 1, dp[i])
        return dp[amount] if dp[amount] != float('inf') else -1 


        
# @lc code=end



coinChange = Solution().coinChange

print(coinChange([2], 3))
print(coinChange([1,2,5], 11))
print(coinChange([1], 0))
