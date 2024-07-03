#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # 结束前面链表 这是关键
        prev.next = None

        p = self.sortList(head)
        q = self.sortList(slow)


        return self.merge(p, q)

    

    def merge(self, p, q):

        dummy = ListNode()
        cur = dummy

        while p and q:

            if p.val < q.val:
                cur.next = p
                p = p.next
            else:
                cur.next = q
                q = q.next
            cur = cur.next

        
        if p:
            cur.next = p

        if q:
            cur.next = q


        return dummy.next


        
# @lc code=end

# import test
# test.test(Solution().sortList, test.CreateLinkedList([4,2,1,3]))
# test.test(Solution().sortList, test.CreateLinkedList([1,2,3,4]))