#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.

from typing import List, Optional

#  一个更简洁的方案，preorder直接修改
def buildTree(self, preorder, inorder):
    if inorder:
        ind = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[ind])
        root.left = self.buildTree(preorder, inorder[0:ind])
        root.right = self.buildTree(preorder, inorder[ind+1:])
        return root

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        rootval = preorder[0]
        rootidx = inorder.index(rootval)

        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1:1+rootidx], inorder[:rootidx])
        root.right = self.buildTree(preorder[1+rootidx:], inorder[rootidx+1:])

        return root


# @lc code=end
