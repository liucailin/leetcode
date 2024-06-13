#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, k = 0, len(nums)
        n = 0
        while i < k:
            if nums[i] == val:
                nums[i] = None
                n += 1
            i += 1

        i, j = 0, k - 1
        while i < j:
            if nums[i] == None:
                while j > i and nums[j] == None:
                    j -= 1
                if j > i:
                    nums[i], nums[j] = nums[j], nums[i]
                    j -= 1
            i += 1

        return  k - n

        
# @lc code=end

print(Solution().removeElement([2,3,3],3))