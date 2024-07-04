#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
from typing import List


# 找左侧
def find_left(nums, target):
    n = len(nums)
    left, right = 0, n - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if left == n: return -1
    return left if nums[left] == target else -1

# 找右侧
def find_right(nums, target):
    n = len(nums)
    left, right = 0, n - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    if right < 0: return -1
    return right if nums[right] == target else -1


def find_middle_and_search(nums, target):
    n = len(nums)
    left, right = 0, n - 1

    while left <= right:
        mid = (left + right) // 2
        

        # 找到目标 两边扩散
        if nums[mid] == target:
            i = j = mid
            while i >= 0 and nums[i] == target:
                i -= 1
            while j < n and nums[j] == target:
                j += 1

            return [i + 1, j - 1]
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return [-1,-1]


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        
        return find_middle_and_search(nums, target)
        # 左右找能保证 logN
        # return [find_left(nums, target), find_right(nums, target)]
# @lc code=end

import test
fn = test.createTest(Solution().searchRange)
fn([2,2], 3)
fn([2,2], 2)
fn([5,7,7,8,8,10], 8)
fn([5,7,7,8,8,8,8,10], 8)
fn([5,7,7,8,8,10], 7)
fn([1], 1)