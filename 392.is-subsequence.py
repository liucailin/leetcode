#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if not s:
            return True
        if len(s) > len(t):
            return False
        
        j = 0
        for i in range(len(t)):
            if j < len(s) and t[i] == s[j]:
                j += 1
        
        return j == len(s)
        
# @lc code=end

# from test import test
# test(Solution().isSubsequence, "abc", "ahbgdc")