#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

from collections import deque

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []

        def traverse(root):
            if not root:
                result.append("null")
                return

            result.append(str(root.val))
            traverse(root.left)
            traverse(root.right)


        traverse(root)
        return ','.join(result)


        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        input = data.split(',')

        q = deque(input)

        def traverse(nodes):

            if not nodes:
                return None
            first = nodes.popleft()
            if first == 'null':
                return None

            root = TreeNode(int(first))
            root.left = traverse(nodes)
            root.right = traverse(nodes)
            return root


        return traverse(q)
        

# Your Codec object will be instantiated and called as such:
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.right.left = TreeNode(4)
# root.right.right = TreeNode(5)
# ser = Codec()
# deser = Codec()
# s = ser.serialize(root)
# print(s)
# ans = deser.deserialize(s)
# print(ans)
# @lc code=end

