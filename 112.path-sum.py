#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        self.result = False

        def dfs(node, sum):
            if not node:
                return
            
            if not node.left and not node.right and sum + node.val == targetSum:
                self.result = True
                return
            
            dfs(node.left, sum + node.val)
            dfs(node.right, sum + node.val)


        if root:
            dfs(root, 0)

        return self.result
            

        



# import test

# fn = test.createTest(Solution().hasPathSum)

# fn(test.CreateTreeNode([1, 2]), 2)
# fn(test.CreateTreeNode([1, 2]), 1)
# fn(test.CreateTreeNode([5,4,8,11,None,13,4,7,2,None,None,None,1]), 22)