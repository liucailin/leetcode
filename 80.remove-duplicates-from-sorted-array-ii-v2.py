#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(2, len(nums)):
            if nums[i] != nums[k-1]:
                k += 1
                nums[k] = nums[i]
        return k+1
# @lc code=end

def test(nums):
    print(nums)
    result = Solution().removeDuplicates(nums)
    print(nums, result)

test([1,1,1,2,2,3])
test([0,0,1,1,1,1,2,3,3])