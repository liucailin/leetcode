#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if left == right:
            return head

        cur = head
        prev = None
        k = 1

        start, prev_start = None, None
        tail = None

        while cur:

            next = cur.next
            if k >= left and k <= right:
                if k == left:
                    prev_start = prev
                    start = cur
                elif k == right:
                    tail = cur
                    start.next = cur.next
                cur.next = prev

            prev = cur
            cur = next
            k += 1

        if prev_start:
            prev_start.next = tail


        return tail if left == 1 else head
        
        
# @lc code=end

import test

fn = test.createTest(Solution().reverseBetween)
# fn(test.CreateLinkedList([1,2,3,4,5]), 2, 4)
fn(test.CreateLinkedList([1,2,3,4,5]), 1, 5)
fn(test.CreateLinkedList([1,2,3,4,5]), 1, 4)
fn(test.CreateLinkedList([1,2,3,4,5]), 2, 5)
fn(test.CreateLinkedList([5]), 1, 1)
