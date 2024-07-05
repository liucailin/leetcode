#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#


# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}

        for c in s:
            count[c] = count.get(c, 0) + 1

        for c in t:
            if c in count:
                count[c] -= 1
            else:
                count[c] = count.get(c, 0) + 1


        for val in count.values():
            if val != 0:
                return False
        
        return True
        

        
# @lc code=end

