#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        for digit in digits:
            number = number * 10 + digit

        number += 1

        plus = []
        while number:
            plus.append(number % 10)
            number = number // 10

        plus.reverse()
        return plus
# @lc code=end


print(Solution().plusOne([9]))