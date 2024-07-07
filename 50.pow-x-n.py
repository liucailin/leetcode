#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

def myPower_memo(x, n):
    """
    我的解法 使用备忘录剪枝
    """
    if n == 0:
        return 1
    sign = 1 if n > 0 else -1
    n = abs(n)

    memo = {}

    def bi_power(x, n):
        if n in memo:
            return memo[n]
        elif n == 0:
            return 1
        elif n == 1:
            return x
        elif n == 2:
            return x * x
        else:
            a = bi_power(x, n // 2)
            memo[n // 2] = a
            b = bi_power(x, n - n // 2)
            memo[n - n // 2] = b
            return  a * b
        
    
    if sign == 1:
        return bi_power(x, n)
    else:
        return 1 / bi_power(x, n)


def myPower_Rec(x, n):
    """
    递归
    """
    if n == 0:
        return 1

    def quickPower(x, n):
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n == 2:
            return x * x
        else:
            p = quickPower(x, n // 2)
            return p * p if n % 2 == 0 else p * p * x
        
    
    if n > 0:
        return quickPower(x, n)
    else:
        return 1.0 / quickPower(x, -n)
    

def myPower_Rec_NoHelper(x, n):
    """
    不用辅助函数, 根据power的定义
    """
    if n == 0:
        return 1
    if n < 0:
        x = 1 / x
        n = -n
    if n % 2 == 0:
        return myPower_Rec_NoHelper(x * x, n // 2)
    else:
        return myPower_Rec_NoHelper(x * x, n // 2) * x


    

def myPowr_iter(x, n):
    """
    迭代
    """
    if n == 0:
        return 1
    if n < 0:
        n = -n
        x = 1 / x
    
    pow = 1
    while n:
        if n & 1:
            pow *= x
        x *= x
        n >>= 1
    return pow


# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return myPowr_iter(x, n)
        



myPowr  = Solution().myPow
print(myPowr(2.00000, 3))
# print(myPowr(2.00000, 2))
# print(myPowr(2.00000, 4))
# print(myPowr(2.00000, 10))
# print(myPowr(2.10000, 3))
# print(myPowr(2.00000, -2))
# print(myPowr(2.00000, 100))
# @lc code=end

