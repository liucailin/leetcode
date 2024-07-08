#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#

# @lc code=start
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            total = sum((num >> i) & 1 for num in nums)
            if total % 3:
                # Python中的整数没有固定的位数限制，但补码运算常用于32位或64位整型。
                # 在处理32位补码时，如果最高位（第31位）为1，则说明该数是负数。
                if i == 31:
                    ans -= (1 << i)
                else:
                    ans |= (1 << i)

        
        return ans
        
# @lc code=end

print(Solution().singleNumber([-2,-2,1,1,4,1,4,4,-4,-2]))