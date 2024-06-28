#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
# 用队列做层级遍历

# @lc code=start

# Definition for a Node.
from typing import Optional
from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        
        queue = deque()
        queue.append(root)

        while queue:

            prev = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if prev:
                    prev.next = node
                prev = node
                
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            prev.next = None

        return root


        
# @lc code=end

