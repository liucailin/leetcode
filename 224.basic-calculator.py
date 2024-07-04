#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        
        stack = []

        result = 0
        number = 0
        sign = 1

        for c in s:
            if str.isdigit(c):
                number = number * 10 + int(c)
            elif c == '+':
                result += number * sign
                number = 0
                sign = 1
            elif c == '-':
                result += number * sign
                number = 0
                sign = -1
            elif c == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif c == ')':
                result += number * sign
                number = 0
                result *= stack.pop()
                result += stack.pop()

        result += number * sign
        
        return result


        
# @lc code=end
    
import test
fn = test.createTest(Solution().calculate)

# fn("1 + 1")
# fn(" 2-1 + 2 ")
fn("(1+(4+5+2)-3)+(6+8)")
fn("2147483647")

