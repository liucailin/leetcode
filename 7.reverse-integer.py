#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        num = abs(x)
        while num:
            r = num % 10
            result += r
            num = num // 10
            if num:
                result *= 10

        return result * (1 if x >= 0 else -1)
        
# @lc code=end

# from test import test
# test(Solution().reverse, 123)
# test(Solution().reverse, -123)
# test(Solution().reverse, 120)