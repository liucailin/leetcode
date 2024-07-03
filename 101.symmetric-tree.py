#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        def symmetricTree(p, q):
            if p and q:
                print(p.val, q.val)
                return p.val == q.val and symmetricTree(p.left, q.right) and symmetricTree(p.right, q.left)
            else:
                return p == q
                

        return symmetricTree(root.left, root.right)
        
        
# @lc code=end


# node = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
# node = TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(4)))
# print(Solution().isSymmetric(node))
