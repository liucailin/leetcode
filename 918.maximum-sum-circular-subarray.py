#
# @lc app=leetcode id=918 lang=python3
#
# [918] Maximum Sum Circular Subarray
#

# @lc code=start
from typing import List


def maxSubarray(nums):
    sum = cursum = nums[0]
    for i in range(1, len(nums)):
        cursum = max(cursum + nums[i], nums[i])
        sum = max(sum, cursum)

    return sum


def minSubarray(nums):
    sum = cursum = nums[0]
    for i in range(1, len(nums)):
        cursum = min(cursum + nums[i], nums[i])
        sum = min(sum, cursum)

    return sum


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        max(maxsum, sum - minsum)
        """
        maxSum = maxSubarray(nums)

        # <0 说明数组全是负数，这时候maxSum直接是最大的
        if maxSum < 0:
            return maxSum

        minSum = minSubarray(nums)
        arraySum = sum(nums)

        return max(maxSum, arraySum - minSum)

        
# @lc code=end

print(Solution().maxSubarraySumCircular([-3,-2,-3]))
print(Solution().maxSubarraySumCircular([1,-2,3,-2]))
print(Solution().maxSubarraySumCircular([5,-3,5]))