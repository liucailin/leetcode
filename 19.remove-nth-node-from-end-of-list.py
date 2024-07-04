#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not n:
            return head
        
        sz = 0
        cur = head
        while cur:
            cur = cur.next
            sz += 1

        # 使用虚拟头简化，因为删除的可能是head节点
        dummy = ListNode(0, head)
        cur = dummy
        for i in range(sz - n ):
            cur = cur.next


        cur.next =  cur.next.next


        return dummy.next
        
# @lc code=end

import test
fn = test.createTest(Solution().removeNthFromEnd)

fn(test.CreateLinkedList([1,2,3,4,5]),2)
fn(test.CreateLinkedList([1]), 1)
fn(test.CreateLinkedList([1,2]), 1)
fn(test.CreateLinkedList([1,2]), 2)