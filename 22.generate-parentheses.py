#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
 

        result = []
        path = []

        def dfs(open, close):
            if len(path) == n * 2:
                result.append(''.join(path))
                return
            
            if open < n:
                path.append('(')
                dfs(open + 1, close)
                path.pop()

            # 注意这里的判断
            if close < open:
                path.append(')')
                dfs(open, close + 1)
                path.pop()


            
        dfs(0, 0)
        return result

        
# @lc code=end

print(Solution().generateParenthesis(1))
print(Solution().generateParenthesis(2))
print(Solution().generateParenthesis(3))