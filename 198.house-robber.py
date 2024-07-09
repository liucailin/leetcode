#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#


def rob(self, nums):
    """
    动态规划
    用二维dp数组分别表示不抢和抢
    可以多次不抢
    第i间房间不抢，最大金额为上一次不抢和上一次抢的最大值
    dp[i][0] = max(dp[i-1][0], dp[i-1][1])
    
    第i间房间抢，i的金额加上上一次不抢的金额
    dp[i][1] = nums[i] + dp[i-1][0]
    """
    n = len(nums)
    if n == 1:
        return nums[0]
    
    dp = [[0 for i in range(2)] for j in range(n)]
    dp[0][0] = 0
    dp[0][1] = nums[0]

    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1])
        dp[i][1] = nums[i] + dp[i-1][0]

    return max(dp[-1][0], dp[-1][1])



def rob1(nums):
    """
     dp[i] 表示前 i 间房屋能偷窃到的最高总金额
     dp[i]=max(dp[i-2]+nums[i],dp[i-1])
    """
    n = len(nums)
    if n == 1:
        return nums[0]
    
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1]) 

    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])

    return dp[-1]

# @lc code=start

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return nums[0]

        norob = 0
        rob = nums[0]

        for i in range(1, n):
            norob, rob = max(rob, norob), nums[i] + norob

        return max(rob, norob)
            
        
# @lc code=end

rob = rob1
test = lambda nums: print(nums, rob(nums))

test([1,2,3,1])
test([2,1,1,2])
test([2,7,9,3,1])