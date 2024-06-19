#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
# 不要求 i,j,k 连续
# 贪心算法 是真没想到

# @lc code=start
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if not nums:
            return False
        n = len(nums)
        if n < 3:
            return False
        
        first = nums[0]
        second = float('inf')
        k = 0
        for i in range(1, n):
            num = nums[i]
            if num > second:
                return True
            if num > first:
                second = first
            else:
                first = num

            
        return False
        
# @lc code=end

from test import test

# test(Solution().increasingTriplet, [2,1,5,0,4,6])
test(Solution().increasingTriplet, [20,100,10,12,5,13])