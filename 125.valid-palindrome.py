#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        if n <= 1:
            return True
        i, j = 0, n - 1
        while i < j:
            if not str.isalnum(s[i]):
                i += 1
                continue
            if not str.isalnum(s[j]):
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1

        return True


# @lc code=end

# Solution().isPalindrome("A man, a plan, a canal: Panama")