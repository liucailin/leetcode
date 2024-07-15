#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        s[i,j]三种情况下是回文
        1. i == j
        2. j-1 == 1 
        3. s[i] == s[j] 且 s[i+1, j-1]是回文
        
        要从下到上，从左到右遍历，这样保证dp[i + 1][j - 1]都是经过计算的
        """
        dp = [[False] * len(s) for _ in range(len(s))]
        maxlenth = 0
        left = 0
        right = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[j] == s[i]:
                    if j - i <= 1 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                if dp[i][j] and j - i + 1 > maxlenth:
                    maxlenth = j - i + 1
                    left = i
                    right = j
        return s[left:right + 1]


# @lc code=end


def test(s): return print(s, Solution().longestPalindrome(s))


test("babad")
test("babab")
test("cbbd")
