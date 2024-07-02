#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
from typing import List

#  滑动窗口，注意窗口收缩，对比我原来的思路
def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        current_sum = 0
        left = 0

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                min_len = min(min_len, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else 0


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)

        i, j = 0, 0
        sum = 0

        min_len = float('inf')

        while j < n:
            next = sum + nums[j]
            if next >= target:
                min_len = min(min_len, j - i + 1)
                sum -= nums[i]
                i += 1
            else:
                sum = next
                j += 1



        return min_len if min_len != float('inf') else 0
                
        
# @lc code=end

from test import createTest
fn = createTest(Solution().minSubArrayLen)
fn(7, [2,3,1,2,4,3])
fn(4, [1,4,4])
fn(11, [1,1,1,1,1,1,1,1])
fn(11, [1,2,3,4,5])
fn(6, [10,2,3])
fn(7, [8])