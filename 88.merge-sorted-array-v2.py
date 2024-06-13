#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# 逆向双指针
# 重点是逆向和处理剩余数组


# @lc code=start
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m - 1, n - 1, m + n -1

        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1


        while j >= 0:
            nums1[j] = nums2[j]
            j -= 1


        return nums1
            
        
        
# @lc code=end


print(Solution().merge([-1,0,0,3,3,3,0,0,0],6,[-2,-2,-2],3))

