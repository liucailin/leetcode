#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
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
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        # 已经拉平
        left = root.left
        right = root.right

        if left:
            # 将左子树作为右子树
            root.right = left
            # 左子树指向空
            root.left = None

            # 寻找当前右子树末端
            current = root
            while current.right:
                current = current.right

            # 连接到原来的右子树
            current.right = right

        return root
        
# @lc code=end

