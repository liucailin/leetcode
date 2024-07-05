#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        m1 = {}
        m2 = {}
        words = s.split(' ')
        if len(words) != len(pattern):
            return False

        for i in range(len(words)):
            p = pattern[i]
            c = words[i]

            if c in m1 and m1[c] != p:
                return False
            if p in m2 and m2[p] != c:
                return False
            
            m1[c] = p
            m2[p] = c

        return True 
        
# @lc code=end

