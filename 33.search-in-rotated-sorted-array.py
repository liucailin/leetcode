#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
from typing import List


def bisearch(nums, lo, hi, target):
    while lo <= hi:
        mid = (lo + hi) // 2
        find = nums[mid]
        if find == target:
            return mid
        elif find < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1


def find_max(nums, lo, hi):
    """
    错误算法
    """
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < nums[mid + 1]:
            lo = mid + 1
        else:
            return mid
        
    return -1

def find_rotation_point(nums, lo, hi):
    """
    找到旋转点，也就是最小值的点
    """
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid

    return lo



def find_rotation_then_search(nums, target):
    """
    方法 1
    找到旋转点 判断target在哪边再进行二分搜索
    """
    if not nums:
        return -1
    n = len(nums)

    if nums[0] <= nums[-1]:
        return bisearch(nums, 0, n - 1, target)
    
    rotate = find_rotation_point(nums, 0, n - 1)
    if nums[rotate] <= target <= nums[-1]:
        return bisearch(nums, rotate, n - 1, target)
    else:
        return bisearch(nums, 0, rotate - 1, target)


def search_rotated_array(nums, target):
    """
    方法2
    基于一个事实, 数组被mid分开两部分后,一定有一边是有序的
    nums[mid] == target  找到 
    左边有序 且 nums[lo] <= target < nums[mid]  向左收缩   否则   向右
    右边有序 且 nums[mid] < target < nums[hi]   向右收缩   否则   向左
    """
    lo, hi = 0, len(nums) - 1

    while lo <= hi:

        mid = (lo + hi) // 2

        if nums[mid] == target:
            return mid
        # 左边有序
        if nums[lo] <= nums[mid]:
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        # 右边有序
        else:
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1




        

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return search_rotated_array(nums, target)
        # return find_rotation_then_search(nums, target)


        
# @lc code=end

import test
fn = test.createTest(Solution().search)

fn([5,1,3], 1)
fn([1], 1)
fn([4,5,6,7,0,1,2], 0)
fn([4,5,6,7,0,1,2], 6)
fn([4,5,6,7,0,1,2], 3)
fn([1], 0)


