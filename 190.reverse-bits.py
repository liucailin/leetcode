#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
# 参考
# https://leetcode.cn/problems/reverse-bits/solutions/686320/ju-yi-fan-san-yi-wen-dai-ni-shua-san-dao-ubat/?envType=study-plan-v2&envId=top-interview-150





# @lc code=start



def reverseBits(n: int) -> int:
    """
    类似整数反转 只不过模`10`改成模`2` 且限定 2位
    """
    res = 0
    for _ in range(32):
        res = res * 2 + n % 2
        n //= 2

    return res

def reverseBits(n: int) -> int:
    """
    位运算
    n & 1 取得低位
    res << 1 左移一位 拼接上面步骤取得的低位
    n >> 1 右移一位，为下次循环准备
    """
    res = 0
    for _ in range(32):
        res = (res << 1) | (n & 1)
        n >>= 1
    return res



def reverseBits(n: int) -> int:
    """
    分治
    M1 = 0x55555555 01010101010101010101010101010101
    M2 = 0x33333333 00110011001100110011001100110011
    M4 = 0x0f0f0f0f 00001111000011110000111100001111
    M8 = 0x00ff00ff 00000000111111110000000011111111
    """
    n = (n >> 16) | (n << 16)
    n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
    n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
    n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
    n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)




class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
           res = res * 2 + n % 2
           n //= 2

        return res
        
# @lc code=end


reverseBits = Solution().reverseBits
print(reverseBits(0b00000010100101000001111010011100))
    

