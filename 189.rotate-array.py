#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            nums.insert(0, nums.pop())

        
# @lc code=end
        
# from test import test
# test(Solution().rotate, [1,2,3,4,5,6,7], 3)
# test(Solution().rotate, [-1,-100,3,99], 2)

