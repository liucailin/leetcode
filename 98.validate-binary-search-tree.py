#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return False
        
        self.result = True
        self.val = float('-inf')

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if node.val <= self.val:
                self.result = False
                return
            self.val = node.val
            inorder(node.right)

        inorder(root)
        return self.result

        

        
# @lc code=end

