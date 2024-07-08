#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
from typing import List

digit_to_letter = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        result = []
        path = []

        def dfs(cur):
            if len(path) == len(digits):
                result.append(''.join(path))
                return
            
            for i in range(cur, len(digits)):
                d = digits[i]
                for j in digit_to_letter[d]:
                    path.append(j)
                    dfs(i + 1)
                    path.pop()


        dfs(0)
        return result
        
# @lc code=end

print(Solution().letterCombinations("23"))
print(Solution().letterCombinations("234"))
print(Solution().letterCombinations("2"))