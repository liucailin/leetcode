#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
# 


"""
k 是当前位置 f(k)是最远可达距离

f(k) = k + nums[k]
if k > f(k) 不可达
if f(k) >= n - 1 可达
"""

# @lc code=start
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        furthest = 0
        for i in range(n):
            if i > furthest:
                return False
            furthest = max(furthest, i + nums[i])
            if furthest >= n - 1:
                return True
        return False


# @lc code=end

from test import test
# test(Solution().canJump, [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
# )
# test(Solution().canJump, [2,3,1,1,4])
test(Solution().canJump, [3,0,8,2,0,0,1])
