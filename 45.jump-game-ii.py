#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        step = 0
        current_end = 0
        furthest = 0
        
        for i in range(n - 1):
            furthest = max(furthest, i + nums[i])
            
            if i == current_end:
                step += 1
                current_end = furthest
            
            # 当达到或超过最后一个位置时，直接返回结果。
            if current_end >= n - 1:
                return step

        return step

# @lc code=end

from test import test
test(Solution().jump, [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3])
test(Solution().jump, [1,2,1,1,1])
test(Solution().jump, [2,3,1,1,4])
test(Solution().jump, [2,3,0,1,4])