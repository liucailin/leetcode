#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#

# @lc code=start
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        paths = []
        n = len(graph)

        def dfs(node: int, path: List[int]):

            path.append(node)
            if node == n - 1: 
                paths.append(path[::])

            for neibour in graph[node]:
                dfs(neibour, path)

            path.pop()

        
        dfs(0, [])

        return paths

        
        
# @lc code=end



print(Solution().allPathsSourceTarget([[1,2],[3],[3],[]]))