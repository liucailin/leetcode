#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        path = []
        def dfs(cur, n, k):
            if k == 0:
                result.append(path[:])
                return

            for i in range(cur, n + 1):
                path.append(i)
                dfs(i + 1, n, k - 1)
                path.pop()
        dfs(1, n, k)
        return result


        
# @lc code=end

print(Solution().combine(4, 2))
print(Solution().combine(1, 1))