#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        path = []

        def dfs(node, sum):
            if not node:
                return
            if not node.left and not node.right:
                path.append(sum * 10 + node.val)

            dfs(node.left, sum * 10 + node.val)
            dfs(node.right, sum * 10 + node.val)


        dfs(root, 0)
        return sum(path)
        
# @lc code=end
    

# import test
# fn = test.createTest(Solution().sumNumbers)

# fn(test.CreateTreeNode([1,2,3]))
# fn(test.CreateTreeNode([4,9,0,5,1]))

