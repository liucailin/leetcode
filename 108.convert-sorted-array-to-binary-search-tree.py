#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional
# from test import TreeNode


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def dfs(lo, hi):

            if lo > hi:
                return None

            mid = (lo + hi) // 2
            root = TreeNode(nums[mid])
            root.left = dfs(lo, mid - 1)
            root.right = dfs(mid + 1, hi)

            return root
        

        return dfs(0, len(nums) - 1)
            


# import test

# fn = test.createTest(Solution().sortedArrayToBST)
# fn([-10,-3,0,5,9])
        
# @lc code=end

