#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#

def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        递归式
        n = len(str1)
        m = len(str2)
        base case
            比较两个字符串相等需要O(n)
            T(n, m) = O(n)   if n == m 
            T(n, m) = O(1)   if n != m
        recursive
            T(n, m) = T(n, m - n) + O(n)   if n < m
            T(n, m) = T(m, n - m) + O(m)   if n > m

        故 时间复杂度 T(n) = O(min(n, m)^2)
        """
        if len(str1) == len(str2):
            return str1 if str1 == str2 else ""
        elif len(str1) < len(str2):
            return self.gcdOfStrings(str1, str2[len(str1):]) if str1 == str2[:len(str1)] else ""
        else:
            return self.gcdOfStrings(str2, str1[len(str2):]) if str2 == str1[:len(str2)] else ""

# @lc code=start

def gcdOfStrings_fast(str1: str, str2: str) -> str:
    """
    如果str1和str2有gcd
    则str1+str2 = st2+str1
    如果不用这条性质，求出gcd长度后再判断是否能拼接成str1和str2也可以
    用gcd求出长度即可

    时间复杂度 是 O(n+m)
    """

    if str1 + str2 != str2 + str1:
        return ""

    def gcd(m, n):
        while n:
            m, n = n, m % n
        return m
    
    gcd_len = gcd(len(str1), len(str2))
    return str1[:gcd_len]



class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        return gcdOfStrings_fast(str1, str2)

        
# @lc code=end

gcd = Solution().gcdOfStrings
test = lambda s1, s2: print(s1, s2, gcd(s1, s2))

test("ABCABC", "ABC")
test("ABABAB", "AB")
test("LEET", "CODE")