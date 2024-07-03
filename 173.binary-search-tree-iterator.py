#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.cur = root
        self.stack = []


    def next(self) -> int:

        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left

        node = self.stack.pop()
        self.cur = node.right

        return node.val
        
        

    def hasNext(self) -> bool:
        return self.cur != None or len(self.stack) > 0
        


# Your BSTIterator object will be instantiated and called as such:
        
# from test import CreateTreeNode
# obj = BSTIterator(CreateTreeNode([7, 3, 15, None, None, 9, 20]))
# print(obj.hasNext())
# print(obj.next())
# print(obj.hasNext())
# print(obj.next())
# print(obj.hasNext())
# print(obj.next())
# print(obj.hasNext())
# print(obj.next())
# print(obj.hasNext())
# print(obj.next())
# print(obj.hasNext())
# print(obj.hasNext())
# print(obj.hasNext())
# @lc code=end

