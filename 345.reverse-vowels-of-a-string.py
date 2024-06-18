#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        result = list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            left = s[i] in vowels
            right = s[j] in vowels

            if left and right:
                result[i], result[j] = result[j], result[i]
                left = right = False

            if not left:
                i += 1
            if not right:
                j -= 1

        return ''.join(result)
    

# from test import test
# test(Solution().reverseVowels, 'ai')
# test(Solution().reverseVowels, 'leetcode')
# test(Solution().reverseVowels, 'hello')
# test(Solution().reverseVowels, "A man, a plan, a canal: Panama")
        
# @lc code=end

