#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        majority_element = nums[0]
        count = max_count = 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1

            if count > max_count:
                max_count = count
                majority_element = nums[i]
                
        return majority_element
        
# @lc code=end


def test(nums):
    result = Solution().majorityElement(nums)
    print(nums, result)

# test([3,2,3])
# test([2,2,1,1,1,2,2])
    