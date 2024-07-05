#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        m1 = {}
        m2 = {}
        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]

            if c2 in m2 and m2[c2] != c1:
                return False
            
            if c1 in m1 and m1[c1] != c2:
                return False
            
            m2[c2] = c1
            m1[c1] = c2

        return True
# @lc code=end



print(Solution().isIsomorphic("badc", "baba"))
print(Solution().isIsomorphic("foo", "bar"))
print(Solution().isIsomorphic("egg", "add"))
print(Solution().isIsomorphic("paper", "title"))