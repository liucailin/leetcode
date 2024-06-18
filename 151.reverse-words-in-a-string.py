#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        i = 0
        j = len(a) - 1
        while i < j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

        return ' '.join(a)
        
# @lc code=end

