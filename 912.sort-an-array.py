#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#

# @lc code=start
from typing import List
import random

#  冒泡排序 TLE
def bubble_sort(nums):
    n = len(nums)
    # 外循环控制遍历次数
    for i in range(n-1):
        swaped = False
        # 内循环进行两两比较和交换，数组末端的 i 个元素已经是有序的，无需比较
        for j in range(n - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swaped = True

        # 优化：如果内层循环未发生交换，说明数组已经有序
        if not swaped:
            break

# 插入排序 TLE
def insertion_sort(nums):
    n = len(nums)
    # 从第二个元素开始，逐步插入
    for i in range(1, n):
        key = nums[i] # 选中当前要插入的元素
        j = i - 1
        # 从后向前扫描已排序子数组
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j] # 将大于key的元素右移
            j -= 1
        # 插入 key 到正确的位置
        nums[j + 1] = key

    return nums

# 选择排序 TLE
def selection_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if nums[j] < nums[min]:
                min = j
        nums[i], nums[min] = nums[min], nums[i]

# 标准分区算法 对于有序数组会超时 11/21 cases passed (N/A)  [1,2,3,4,5,6,7,...,50000]
def partition(nums, lo, hi):
    
    # 旋转最后一个元素作为基准
    pivot = nums[hi]

    # 临时 pivot index
    i = lo
    for j in range(lo, hi):
        if nums[j] < pivot:
            nums[j], nums[i] = nums[i], nums[j]
            i += 1

    nums[i], nums[hi] = nums[hi], nums[i]
    return i

# 随机化分区 对于相同元素会超时   17/21 cases passed (N/A)   50000个相同的2 
def random_partition(nums, lo, hi):
    rand = random.randint(lo, hi)
    nums[rand], nums[hi] = nums[hi], nums[rand]
    return partition(nums, lo, hi)
    
# 霍尔分区方案
def hoare_partition(nums, lo, hi):
    pivot = nums[(lo + hi) // 2]
    i = lo
    j = hi
    
    i = lo - 1
    j = hi + 1
    
    while True:
        # 向右移动i，直到找到一个大于或等于pivot的元素
        i += 1
        while nums[i] < pivot:
            i += 1
        
        # 向左移动j，直到找到一个小于或等于pivot的元素
        j -= 1
        while nums[j] > pivot:
            j -= 1
        
        # 如果i和j交错，返回j
        if i >= j:
            return j
        
        # 交换i和j位置的元素
        nums[i], nums[j] = nums[j], nums[i]
           


# 快速排序
def quick_sort(nums):

    def helper(nums, lo, hi):

        if lo < hi:
            p = random_partition(nums, lo, hi)
            # helper(nums, lo, p)

            # 如果是其他分区算法
            helper(nums, lo, p - 1)
            helper(nums, p + 1, hi)

    helper(nums, 0, len(nums) - 1)
    return nums


def merge(nums, lo, mid, hi):
    i = lo
    j = mid + 1

    temp = []
    while i <= mid and j <= hi:
        if nums[i] < nums[j]:
            temp.append(nums[i])
            i += 1
        else:
            temp.append(nums[j])
            j += 1

    
    while i <= mid:
        temp.append(nums[i])
        i += 1

    while j <= hi:
        temp.append(nums[j])
        j += 1


    for i in range(len(temp)):
        nums[lo+i] = temp[i]


# 归并排序
def merge_sort(nums):

    def helper(nums, lo, hi):
        if lo < hi:
            mid = (lo + hi) // 2

            helper(nums, lo, mid)
            helper(nums, mid + 1, hi)

            merge(nums, lo, mid, hi)

        

    helper(nums, 0, len(nums) - 1)

    return nums



class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        merge_sort(nums)
        return nums
        
# @lc code=end





from test import test
test(merge_sort, [5,2,3,1])
test(merge_sort,  [5,1,1,2,0,0])
test(merge_sort,  [-1,2,-8,-10])
test(merge_sort,  [-2,3,-5])