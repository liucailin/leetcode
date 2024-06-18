#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
from typing import List



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        product = 1
        n = len(nums)
        for i in range(n):
            answer[i] = product
            product *= nums[i]

        product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= product
            product *= nums[i]

        return answer
        
# @lc code=end

# from test import test
# test(Solution().productExceptSelf, [1,2,3,4])