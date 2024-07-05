#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(nums)):
            n = nums[i]

            if n in m:
                return [m[n], i]
            else:
                m[target - n] = i 
        
# @lc code=end

