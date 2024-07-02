#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 双指针迭代
def reverseList_iter(head: Optional[ListNode]):
    cur = head
    prev = None
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev

def reverseList_rec(head: Optional[ListNode]):
    if not head or not head.next:
        return head
    
    newhead = reverseList_rec(head.next)
    head.next.next = head
    head.next = None
    return newhead

# 后序，我的解法
def reverseList(head: Optional[ListNode]):
    if not head or not head.next:
        return head
    rev = reverseList(head.next)
    cur = rev
    while cur.next:
        cur = cur.next
    cur.next = head
    head.next = None

    return rev


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return reverseList_iter(head)


from test import test, LinkedList
test(Solution().reverseList, LinkedList([1,2,3,4,5]))
        
# @lc code=end

