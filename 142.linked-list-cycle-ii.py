#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

        if not fast or not fast.next:
            return None
        
        slow = head
        while fast != slow:
            fast = fast.next
            slow = slow.next

        return slow


            
        
# @lc code=end

# a = ListNode(3)
# b = ListNode(2)
# c = ListNode(0)
# d = ListNode(-4)

# a.next = b
# b.next = c
# c.next = d
# d.next = b

# Solution().detectCycle(a)