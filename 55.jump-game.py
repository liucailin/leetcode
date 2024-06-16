#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
from typing import List

# 使用递归 超时
def canJump_Recursive(nums: List[int]) -> bool:
    if len(nums) == 1:
        return True
    if nums[0] == 0:
        return False

    for i in range(nums[0]):
        if canJump_Recursive(nums[i+1:]):
            return True
    return False

# 使用递归（辅助函数）超时
def canJump_Recursive_Helper(nums: List[int]) -> bool:
    n = len(nums)

    def jump(k):
        if k >= n - 1:
            return True
        if nums[k] == 0:
            return False

        furthest = min(k + nums[k], n - 1)
        for i in range(k + 1, furthest + 1):
            if jump(i):
                return True
        return False

    return jump(0)

# 使用递归 (记忆化) 超时
def canJump_Recursive_Memo(nums: List[int]) -> bool:
    memo = {}
    n = len(nums)

    def jump(k):
        if k in memo:
            return memo[k]
        if k >= n - 1:
            return True
        if nums[k] == 0:
            return False

        furthest = min(k + nums[k], n - 1)
        for i in range(k + 1, furthest + 1):
            if jump(i):
                memo[i] = True
                return True
        memo[k] = False
        return False

    return jump(0)

# 使用stack模拟递归 超时
def canJump_Stack(nums: List[int]) -> bool:
    n = len(nums)
    if n == 1:
        return True

    stack = [0]

    while stack:
        k = stack.pop()
        if k >= n - 1:
            return True

        furthest = min(k + nums[k], n - 1)
        for i in range(k + 1, furthest + 1):
            stack.append(i)

    return False

# 使用stack模拟递归，同时记忆化，通过
def canJump_Stack_Memo(nums: List[int]) -> bool:
    n = len(nums)
    if n == 1:
        return True

    stack = [0]
    visited = set()

    while stack:
        k = stack.pop()
        if k >= n - 1:
            return True

        furthest = min(k + nums[k], n - 1)
        for i in range(k + 1, furthest + 1):
            if i not in visited:
                stack.append(i)
                visited.add(i)

    return False


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return canJump_Stack(nums)


# @lc code=end

# from test import test
# test(Solution().canJump, [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
# )
# test(Solution().canJump, [2,3,1,1,4])
# test(Solution().canJump, [3,2,1,0,4])
