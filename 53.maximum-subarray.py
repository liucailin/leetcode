#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#


def maxSubArray(nums):
    """
    Kadane's Algorithm
    状态定义
    设 dp[i] 表示以元素 nums[i] 结尾的最大子数组和。

    状态转移方程
    对于每个元素 nums[i]，有两种选择：
    1. 将 nums[i] 添加到前面的子数组中。
    2. 从 nums[i] 开始一个新的子数组。
    因此，状态转移方程为：
    dp[i]=max(nums[i],dp[i-1]+nums[i])
    """
    dp = [0] * len(nums)
    dp[0] = nums[0]

    max_sum = dp[0]

    for i in range(1, len(nums)):
        dp[i] = max(dp[i-1] + nums[i], nums[i])
        max_sum = max(max_sum, dp[i])

    return max_sum

# @lc code=start
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Kadane
        根据「状态转移方程」, dp[i] 的值只和 dp[i - 1] 有关，因此可以使用「滚动变量」的方式将
        """

        sum = cursum = nums[0]
        for i in range(1, len(nums)):
            cursum = max(cursum + nums[i], nums[i])
            sum = max(sum, cursum)

        return sum
        
# @lc code=end


maxSubArray = Solution().maxSubArray
test = lambda n: print(n, maxSubArray(n))

test([-2,1,-3,4,-1,2,1,-5,4])
test([1,2])
test([1])
test([5,4,-1,7,8])
