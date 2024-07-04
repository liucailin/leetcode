#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)


        prev = dummy
        cur = head

        while cur:

            duplicate = False
            while cur.next and cur.next.val == cur.val:
                cur = cur.next
                duplicate = True

            if duplicate:
                prev.next = cur.next
            else:
                prev = cur                


            cur = cur.next


        return dummy.next
        
# @lc code=end

import test

fn = test.createTest(Solution().deleteDuplicates)

# fn(test.CreateLinkedList([1,2,3,3,4,4,5]))
fn(test.CreateLinkedList([1,1,1,2,3]))
