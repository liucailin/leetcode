#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        a xor 0 = a
        a xor a = 0
        """
        ans = 0
        for n in nums:
            ans ^= n

        return ans
        
# @lc code=end

