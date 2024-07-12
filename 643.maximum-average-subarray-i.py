#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxsum = 0
        for i in range(k):
            maxsum += nums[i]
        cursum = maxsum
        for i in range(k, len(nums)):
            cursum = cursum + nums[i] - nums[i-k]
            maxsum = max(maxsum, cursum)

        return maxsum / k
        
# @lc code=end


findMaxAverage = Solution().findMaxAverage
test = lambda nums, k: print(nums, k, findMaxAverage(nums, k))


test([1,12,-5,-6,50,3], 4)
test([5], 1)