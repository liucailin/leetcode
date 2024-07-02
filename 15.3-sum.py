#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
from typing import List


class Solution:


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        for i in range(len(nums) - 2):
            first = nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                second = nums[j]
                third = nums[k]

                sum = first + second + third

                if sum == 0:
                    result.add((first, second, third))
                    j += 1
                    k -= 1
                elif sum < 0:
                    j += 1
                else:
                    k -= 1

        return result


        
# @lc code=end

# print(Solution().threeSum([-1,0,1,2,-1,-4]))