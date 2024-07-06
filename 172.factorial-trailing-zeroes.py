#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#

# @lc code=start


def trailingZeroes(n):
    """
    0 必定由 2 * 5 产生
    所以问题转换成求5的倍数个数
    """
    ans = 0
    for i in range(5, n + 1, 5):
        while i % 5 == 0:
            i //= 5
            ans += 1
    return ans


def trailingZeroes(n):
    """
    优化
    5     每隔 5 个数 出现 1 次
    5*5   每隔 25 个数 出现 1 次
    5*5*5 每隔 125 个数 出现 1 次
    """
    ans = 0
    while n:
        n //= 5
        ans += n
    return ans


def trailingZeroes(n):
    """
    递归实现
    """
    return 0 if n == 0 else n // 5 + trailingZeroes(n // 5)


def trailingZeroes(n):
    """
    直接算出来
    """
    return n//5 + n//25 + n//125 + n//625 + n//3125


class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0

        factorial = 1

        for i in range(2, n + 1):
            factorial *= i

        zeros = 0

        while factorial:
            if factorial % 10 == 0:
                zeros += 1
                factorial = factorial // 10
            else:
                break

        return zeros

# @lc code=end


# print(Solution().trailingZeroes(5))
