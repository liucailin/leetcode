#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional





class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy



        add = 0

        while l1 and l2:

            res = l1.val + l2.val + add
            add = res // 10
            cur.next = ListNode(res % 10)

            l1 = l1.next
            l2 = l2.next
            cur = cur.next

        left = l1 if l1 else l2

        while left:
            res = left.val + add
            add = res // 10
            cur.next = ListNode(res % 10)

            left = left.next
            cur = cur.next

        if add:
            cur.next = ListNode(add)


        return dummy.next
        
# @lc code=end

# import test

# fn = test.createTest(Solution().addTwoNumbers)
# fn(test.CreateLinkedList([2,4,3]), test.CreateLinkedList([5,6,4]))
# fn(test.CreateLinkedList([0]), test.CreateLinkedList([0]))
# fn(test.CreateLinkedList([9,9,9,9,9,9,9]), test.CreateLinkedList([9,9,9,9]))
# fn(test.CreateLinkedList([2,4,9]), test.CreateLinkedList([5,6,4,9]))
