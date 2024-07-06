#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        p = 0
        n = x
        while n:
            p = p * 10 + n % 10
            n = n // 10

        return p == x
        
# @lc code=end

print(Solution().isPalindrome(0))
print(Solution().isPalindrome(121121))
print(Solution().isPalindrome(10))
print(Solution().isPalindrome(-222))