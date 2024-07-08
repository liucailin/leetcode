#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#

# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
        寻找left和right的公共前缀
        """
        while left < right:
            right = right & (right - 1)

        return right
        
        
# @lc code=end


# print(Solution().rangeBitwiseAnd(600000000, 2147483647))






