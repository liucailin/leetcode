#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        slow, fast = 0, len(numbers) - 1
        while slow < fast:
            sum = numbers[slow] + numbers[fast]
            if sum == target:
                return [slow + 1, fast + 1]
            elif sum < target:
                slow += 1
            else:
                fast -= 1

        return [None, None]
            
        
# @lc code=end

