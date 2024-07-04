#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not k:
            return head
        sz = 0
        cur = head
        tail = None
        while cur:
            sz += 1
            tail = cur
            cur = cur.next

        k = k % sz
        if k == 0:
            return head
        
        cur = head
        
        for i in range(sz - k - 1):
            cur = cur.next

        newhead = cur.next
        cur.next = None
        tail.next = head

        return newhead


        
        
# @lc code=end

import test

fn = test.createTest(Solution().rotateRight)
fn(test.CreateLinkedList([1,2,3,4,5]), 2)
fn(test.CreateLinkedList([0,1,2]), 4)