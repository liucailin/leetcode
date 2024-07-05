#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#

# @lc code=start
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1

        return nums[left]

        
# @lc code=end


print(Solution().findMin([1,3,3]))
print(Solution().findMin([3,3,1,3]))
print(Solution().findMin([1,3,5]))
print(Solution().findMin([2,2,2,0,1]))