#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start



def newton_sqrt(x):
    if x == 0:
        return 0
    
    c = x
    x0 = x

    while True:
        # x1 = x0 - (x0 * x0 - c) / (2 * x0)
        # x1 = x0 - 0.5 * (x0 - c / x0)
        x1 = 0.5 * (x0 + c / x0)
        if abs(x1 - x0) < 1e-7:
            break
        x0 = x1

    return int(x0)
        


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        lo, hi = 2, x // 2

        while lo <= hi:
            mid = (lo + hi) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square < x:
                lo = mid + 1
            else:
                hi = mid - 1

        return hi


        
        

    
        
# @lc code=end



mysqrt = newton_sqrt
print(mysqrt(2))
print(mysqrt(8192))
for i in range(20):
    print(f'sqrt({i}) = {i ** 0.5} mysqrt({i}) = {mysqrt(i)}')