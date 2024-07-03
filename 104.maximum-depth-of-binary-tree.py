#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = 1 + self.maxDepth(root.left)
        right = 1 + self.maxDepth(root.right)

        return max(left, right)
# @lc code=end

# node = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
# print(Solution().maxDepth(node))