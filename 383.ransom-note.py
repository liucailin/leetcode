#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = {}
        for c in magazine:
            m[c] = m.get(c, 0) + 1

        for c in ransomNote:
            if c not in m:
                return False
            if m[c] == 0:
                return False
            m[c] = m[c] - 1

        return True

        
# @lc code=end

