#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

def hammingWeight(n: int) -> int:
    """
    Brian Kernighan 
    n & (n - 1) ，可以把 n 的二进制中，最后一个出现的 1 改写成 0
    https://leetcode.cn/problems/number-of-1-bits/solutions/672418/fu-xue-ming-zhu-xiang-jie-wei-yun-suan-f-ci7i/?envType=study-plan-v2&envId=top-interview-150
    """
    res = 0
    while n:
        res += 1
        n &= n - 1
    return res



# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for _ in range(32):
            count += n & 1
            n >>= 1

        return count
        
# @lc code=end




fn = lambda n: print(Solution().hammingWeight(n))

fn(11)
fn(128)
fn(2147483645)
