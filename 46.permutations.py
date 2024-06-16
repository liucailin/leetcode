#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        used = [False for _ in range(n)]

        def backtrack(track: List[int], depth):
            if len(track) == n:
                result.append(track[:])
                return
            
            for i in range(n):
                if used[i]:
                    continue
                track.append(nums[i])
                used[i] = True
                backtrack(track, depth + 1)
                track.pop()
                used[i] = False

        backtrack([], 0)

        return result
        
# @lc code=end
    
# from test import test
# test(Solution().permute, [1,2,3])

