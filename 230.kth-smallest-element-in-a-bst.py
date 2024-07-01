#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.result = 0
        self.rank = 0
        def dfs(root, k):
            if not root:
                return
            dfs(root.left, k)
            self.rank += 1
            if k == self.rank:
                self.result = root.val
                return
            dfs(root.right, k)


        dfs(root, k)
        return self.result
        
# @lc code=end

