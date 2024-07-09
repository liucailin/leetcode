#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

def climbStairs(self, n: int) -> int:
    """
    TLE 44
    """

    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    return self.climbStairs(n - 1) + self.climbStairs(n - 2)


def climbStairs(self, n: int) -> int:
    """
    AC 使用备忘录
    """
    memo = {}

    def climb(n):
        if n in memo:
            return memo[n]
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        one = climb(n - 1)
        memo[n - 1] = one
        two = climb(n - 2)
        memo[n - 2] = two
        return one + two

    return climb(n)

def climbStairs(self, n: int) -> int:
    """
    动态规划
    dp[i]表示到第i个阶梯的方式
    要到达第 n 阶
    可以从第 n-1 阶走1步到达
    也可以从第 n-2 阶走2步到达
    因此，到达第 n 阶的方法数就是到达第 n-1 阶和第 n-2 阶的方法数之和。
    dp[i] = dp[i-1] + dp[i-2]
    """
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


def climbStairs(self, n: int) -> int:
    """
    动态规划优化
    """
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b

    return b

def climbStairs(self, n: int) -> int:
    """
    斐波那契数列
    """
    a = b = 1
    for _ in range(n):
        a, b = b, a + b
    return a

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        a = b = 1
        for _ in range(n):
            a, b = b, a + b
        return a

        
# @lc code=end


print(Solution().climbStairs(2)) # 2
print(Solution().climbStairs(3)) # 3
print(Solution().climbStairs(4)) # 5
print(Solution().climbStairs(44)) # 1134903170