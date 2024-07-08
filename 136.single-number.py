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
        交换律 a xor b  = b xor a
        结合律 (a xor b) xor c = a xor (b xor c)
        自反性 a xor b xor b => a xor (b xor b) = a xor 0 = a
        """
        ans = 0
        for n in nums:
            ans ^= n

        return ans
        
# @lc code=end

