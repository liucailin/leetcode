#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if n == 0:
            return True
        if len(flowerbed) == 1:
            return False if flowerbed[0] == 1 or n > 1 else True

        i = 0
        k = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                planted = False
                
                if i == 0:
                    planted = flowerbed[i+1] == 0
                elif i == len(flowerbed) -1:
                    planted = flowerbed[i-1] == 0
                else:
                    planted = flowerbed[i+1] == flowerbed[i-1] and flowerbed[i-1] == 0
                if planted:
                    flowerbed[i] = 1
                    k+=1
                

            i += 1

        return k >= n

        
# @lc code=end

# from test import test
# test(Solution().canPlaceFlowers, [1,0,0,0,1,0,0], 2)
# test(Solution().canPlaceFlowers, [1,0,0,0,0,1], 2)
# test(Solution().canPlaceFlowers, [1,0,0,0,1], 2)