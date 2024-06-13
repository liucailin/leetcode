#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# 59/59 cases passed (45 ms)
# Your runtime beats 20.46 % of python3 submissions
# Your memory usage beats 64.11 % of python3 submissions (16.5 MB)


# @lc code=start
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = j = 0
        k = len(nums1)
        
        while i < m or j < n:
            c1 = c2 = None
            if i < m:
                c1 = nums1[i]
            if j < n:
                c2 = nums2[j]
            
            t = None
            if c1 != None and c2 != None:
                t = min(c1, c2)
                if t == c1:
                    i += 1
                else:
                    j += 1
            elif c1 != None:
                t = c1
                i += 1
            else:
                t = c2
                j += 1
            


            nums1.append(t)
        
        i = 0
        while i < k:
            nums1.pop(0)
            i += 1

        return nums1
            
        
        
# @lc code=end


print(Solution().merge([-1,0,0,3,3,3,0,0,0],6,[1,2,2],3))

