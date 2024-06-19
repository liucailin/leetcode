#
# @lc app=leetcode id=1679 lang=python3
#
# [1679] Max Number of K-Sum Pairs
#

# @lc code=start


from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        pair = dict()
        op = 0
        for i in range(len(nums)):
            num = nums[i]
            if num in pair and pair[num]:
                op += 1
                pair[num] -= 1
            else:
                if k - num not in pair:
                    pair[k-num] = 0
                pair[k-num] += 1

        return op

        
# @lc code=end

# from test import test
# test(Solution().maxOperations, [2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2], 3)
# test(Solution().maxOperations,[3,1,3,4,3], 6)
# test(Solution().maxOperations,[1,2,3,4], 5)