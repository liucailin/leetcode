#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        k = n = m = pn = 0
        for i in range(len(nums)):
            if nums[i] == nums[k]:
                n += 1
                if n >= len(nums) // 2 and n > pn:
                    m = nums[i]
                    pn = n
            else:
                n = 1
                k = i
        return m
        
# @lc code=end


def test(nums):
    result = Solution().majorityElement(nums)
    print(nums, result)

# test([3,2,3])
# test([2,2,1,1,1,2,2])
    