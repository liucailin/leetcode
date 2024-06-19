#
# @lc app=leetcode id=654 lang=python3
#
# [654] Maximum Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        if not nums:
            return None

        maxval = float('-inf')
        index = 0
        for i in range(len(nums)):
            if nums[i] > maxval:
                maxval = nums[i]
                index = i

        root = TreeNode(maxval)
        root.left = self.constructMaximumBinaryTree(nums[:index])
        root.right = self.constructMaximumBinaryTree(nums[index+1:])

        return root


        
# @lc code=end

# from test import test
# test(Solution().constructMaximumBinaryTree, [3,2,1,6,0,5])