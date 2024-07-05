#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        lo, hi = 0, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            num = nums[mid]

            left = nums[mid-1] if mid > 0 else float('-inf')
            right = nums[mid+1] if mid < n - 1 else float('-inf')

            if left < num and num > right:
                return mid
            

            if num < right:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1
             
            
        
# @lc code=end

print(Solution().findPeakElement([1]))
print(Solution().findPeakElement([1,2,3,1]))
print(Solution().findPeakElement([1,2,1,3,5,6,4]))