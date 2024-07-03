#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        return isValid(s)
    


def isValid(s: str):
    stack = []
    for c in s:
        if c == '(':
            stack.append(')')
        elif c == '{':
            stack.append('}')
        elif c == '[':
            stack.append(']')
        elif not stack or stack.pop() != c:
            return False
        
    return len(stack) == 0
        
# 我的解法 不必要的内存开销
def isValid_(s: str) -> bool:
    stack = []
    open = set(['(', '{', '['])
    close = {
        ')': '(',
        '}': '{',
        ']': '[',
    }
    for c in s:
        if c in open:
            stack.append(c)
        elif c in close:
            if not stack or close[c] != stack.pop():
                return False
            

    return len(stack) == 0
        
# @lc code=end

# print(Solution().isValid("(){}}{"))