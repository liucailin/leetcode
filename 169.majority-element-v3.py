#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
# 如果将数组 nums 中的所有元素按照单调递增或单调递减的顺序排序，那么下标为 ⌊n/2⌋  的元素（下标从 0 开始）一定是众数。


# @lc code=start
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
        
# @lc code=end


def test(nums):
    result = Solution().majorityElement(nums)
    print(nums, result)

# test([3,2,3])
# test([2,2,1,1,1,2,2])
    