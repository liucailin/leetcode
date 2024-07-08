#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []

        def dfs(cur, sum):
            if sum > target:
                return
            if sum == target:
                result.append(path[:])
                return

            for i in range(cur, len(candidates)):
                path.append(candidates[i])
                dfs(i, candidates[i] + sum)
                path.pop()


        dfs(0, 0)
        return result
        
# @lc code=end


print(Solution().combinationSum([2,3,6,7], 7))
print(Solution().combinationSum([2,3,5], 8))
print(Solution().combinationSum([2], 1))
