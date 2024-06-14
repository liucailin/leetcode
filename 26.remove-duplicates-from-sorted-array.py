#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
# 双指针 + 排序数组
#

# @lc code=start
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]
        return k+1

        
# @lc code=end

def test(nums):
    print(nums)
    result = Solution().removeDuplicates(nums)
    print(nums, result)

# test([0,0,1,1,1,2,2,3,3,4])
# test([1,1,2])