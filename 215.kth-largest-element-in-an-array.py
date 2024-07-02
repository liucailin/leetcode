#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
import random
from typing import List



def partition(nums, lo, hi):
    pivot = nums[hi]
    i = lo
    for j in range(lo, hi):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[hi] = nums[hi], nums[i]
    return i
    
def random_partition(nums, lo, hi):
    rand = random.randint(lo, hi)
    nums[rand], nums[hi] = nums[hi], nums[rand]
    return partition(nums, lo, hi)


def hoare_partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1

    while True:
        # 从左向右找到第一个大于或等于 pivot 的元素
        i += 1
        while arr[i] < pivot:
            i += 1

        # 从右向左找到第一个小于或等于 pivot 的元素
        j -= 1
        while arr[j] > pivot:
            j -= 1

        # 如果两个指针相遇或交错，返回 j
        if i >= j:
            return j

        # 交换 arr[i] 和 arr[j]
        arr[i], arr[j] = arr[j], arr[i]


def hoare_partition2(nums: List[int], lo: int, hi: int) -> int:
    pivot = nums[lo]
    i, j = lo + 1, hi

    while True:
        while i <= hi and nums[i] < pivot:  # 寻找大于等于 pivot 的元素
            i += 1
        while j >= lo + 1 and nums[j] > pivot: # 寻找小于 pivot 的元素
            j -= 1
        if i >= j:
            break
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1

    nums[lo], nums[j] = nums[j], nums[lo]
    return j
           

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        lo, hi = 0, len(nums) - 1
        k = len(nums) - k
        while lo <= hi:
            if lo == hi:
                return nums[lo]
            p = hoare_partition(nums, lo, hi)
            if p < k:
                lo = p + 1
            elif p >= k:
                hi = p
  

        return nums[lo]  # 当 lo == hi 时，返回该值
        
# @lc code=end

# from test import test
# test(Solution().findKthLargest, [5,2,4,1,3,6,0], 4)