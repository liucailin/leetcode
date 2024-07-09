#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#
def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    """
    TLE O(2^m+n)
    f(i,j) = f(i-1, j-1) + 1 A[i] == B[j]
    f(i,j) = max(f(i-1, j), f(i, j-1)) A[i] != B[j]
    """

    if not text1 or not text2:
        return 0
    
    if text1[0] == text2[0]:
        return self.longestCommonSubsequence(text1[1:], text2[1:]) + 1
    else:
        return max(self.longestCommonSubsequence(text1, text2[1:]), self.longestCommonSubsequence(text1[1:], text2))

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        O(m*n)
        """
        m = len(text1)
        n = len(text2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])


        return dp[-1][-1]

        


        
# @lc code=end

longestCommonSubsequence = Solution().longestCommonSubsequence
test = lambda t1, t2: print(t1, t2, longestCommonSubsequence(t1, t2))

test("abcde", "ace")
test("abc", "abc")
test("abc", "def")
test("pmjghexybyrgzczy", "hafcdqbgncrcbihkd")