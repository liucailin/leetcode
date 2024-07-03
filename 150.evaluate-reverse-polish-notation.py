#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token == '+':
                right = stack.pop()
                left = stack.pop()
                stack.append(left + right)
            elif token == '-':
                right = stack.pop()
                left = stack.pop()
                stack.append(left - right)
            elif token == '*':
                right = stack.pop()
                left = stack.pop()
                stack.append(left * right)
            elif token == '/':
                right = stack.pop()
                left = stack.pop()
                stack.append(int(left / right))
            else:
                stack.append(int(token))

            # print(stack)

        return stack[0]

        
# @lc code=end

# print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))