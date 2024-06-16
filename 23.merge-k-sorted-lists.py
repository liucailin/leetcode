#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        while list1 and list2:
            if list1.val > list2.val:
                current.next = list2
                list2 = list2.next
            else:
                current.next = list1
                list1 = list1.next
            current = current.next
        
        if list1:
            current.next = list1
        
        if list2:
            current.next = list2


        return dummy.next
# 线性合并，时间复杂度是O(kn)
def mergeKListsLinear(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None
        
        result = lists[0]

        for i in range(1, len(lists)):
            result = mergeTwoLists(result, lists[i])

        return result

class Solution:
    # 分治合并，复杂度下降到对数级
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None
        
        def merge(left, right):
             if left == right:
                  return lists[left]
             
             mid = (left + right) // 2
             list1 = merge(left, mid)
             list2 = merge(mid + 1, right)
             return mergeTwoLists(list1, list2)
        
        return merge(0, len(lists) - 1)
        
# @lc code=end

