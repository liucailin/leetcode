#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
# 三次翻转
#

# @lc code=start
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # 处理 k 大于数组长度的情况

        def reverse(nums, i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        
        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)

        
# @lc code=end
        
# from test import test
# test(Solution().rotate, [1,2,3,4,5,6,7], 3)
# test(Solution().rotate, [-1,-100,3,99], 2)

