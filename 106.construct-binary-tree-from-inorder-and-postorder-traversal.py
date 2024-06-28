#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional

#  一个更简洁的方案，postorder直接修改, 注意要先 构建 right， 再构建 left
def buildTree(self, inorder, postorder):
    if inorder:
        i = inorder.index(postorder.pop())
        root = TreeNode(inorder[i])
        root.right=self.buildTree(inorder[i+1:],postorder) 
        root.left=self.buildTree(inorder[:i],postorder) 
        return root


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        if not inorder or not postorder:
            return None
        
        rootvalue = postorder[-1]
        rootindex = inorder.index(rootvalue)

        root = TreeNode(rootvalue)
        root.left = self.buildTree(inorder[:rootindex], postorder[:rootindex])
        root.right = self.buildTree(inorder[rootindex+1:], postorder[rootindex:-1])


        return root
        
# @lc code=end

# from test import test
# test(Solution().buildTree, [9,3,15,20,7], [9,15,7,20,3])