#
# @lc app=leetcode id=889 lang=python3
#
# [889] Construct Binary Tree from Preorder and Postorder Traversal
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
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return None
        
        root = TreeNode(postorder.pop())
        
        if len(preorder) == 1:
            return root
        rightIndex = preorder.index(postorder[-1])
        root.right = self.constructFromPrePost(preorder[rightIndex:], postorder)
        root.left = self.constructFromPrePost(preorder[1:rightIndex], postorder)
        return root
        
# @lc code=end

