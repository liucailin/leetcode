#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
# 想复杂了 想到快排的分区了 链表的特性决定了可以新建头节点去连接 而不是像数组一样通过交换实现

# @lc code=start
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small = ListNode()
        large = ListNode()

        samll_head = small
        large_head = large

        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next
            head = head.next

        large.next = None
        small.next = large_head.next

        return samll_head.next
        
# @lc code=end

