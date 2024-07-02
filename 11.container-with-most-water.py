#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water

# @lc code=start
from typing import List


# 超时了
def maxArea(self, height: List[int]) -> int:
    n = len(height)
    if n <= 1:
        return 0

    def area(i, j):
        h = min(height[i], height[j])
        return h * (j - i)

    maxa = 0
    for j in range(1, n):
        cura = 0
        for i in range(j):
            cur = area(i, j)
            if cur > cura:
                cura = cur

        maxa = max(cura, maxa)

    return maxa


class Solution:

    # 双指针 想不出

    def maxArea(self, height: List[int]) -> int:

        n = len(height)
        if n <= 1:
            return 0
        
        i, j = 0, n - 1
        maxa = 0
        while i < j:
            maxa = max(min(height[i], height[j]) * (j - i), maxa)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return maxa


def test(height):
    print(height, Solution().maxArea(height))


test([1, 2, 4, 3])
test([1, 8, 6, 2, 5, 4, 8, 3, 7])
test([1, 8, 100, 2, 100, 4, 8, 3, 7])
test([1, 0, 0, 0, 0, 0, 0, 2, 2])
test([1, 1])

# @lc code=end
