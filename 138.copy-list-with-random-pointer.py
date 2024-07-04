#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        cur = dummy
        random_map = {}
        while head:
            if head in random_map:
                node = random_map[head]
            else:
                node = Node(head.val)
                random_map[head] = node

            if head.random:
                if head.random not in random_map:
                    # 提前创建
                    random = Node(head.random.val)
                    random_map[head.random] = random

                node.random = random_map[head.random]

            cur.next = node
            cur = cur.next
            head = head.next



        return dummy.next
        
# @lc code=end
    
# a = Node(7)
# b = Node(13)
# c = Node(11)
# d = Node(10)
# e = Node(1)

# a.next = b
# b.next = c
# c.next = d
# d.next = e

# b.random = a
# c.random = e
# d.random = c
# e.random = a

# Solution().copyRandomList(a)
