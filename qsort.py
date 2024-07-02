

def lomuto_partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo
    for j in range(lo, hi):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[hi], arr[i] = arr[i], arr[hi]
    return i


def hoare_partition(arr, lo, hi):
    """
    原始的hoare微调版，可以兼容 p - 1 p + 1
    """
    pivot = arr[lo]

    i = lo + 1
    j = hi

    while True:
        while i < hi and arr[i] < pivot:
            i += 1

        while j > lo and arr[j] > pivot:
            j -= 1

        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]

    arr[lo], arr[j] = arr[j], arr[lo]
    return j


def hoare_partition2(arr, lo, hi):
    """
    这个版本很常见，但是不推荐使用，第一要先j--
    第二判断一定要 >= <= , 对于重复元素性能不好
    """
    pivot = arr[lo]

    i = lo
    j = hi

    while i < j:

        # 注意要先 j-- 
        while i < j and arr[j] >= pivot:
            j -= 1

        while i < j and arr[i] <= pivot:
            i += 1

        arr[i], arr[j] = arr[j], arr[i]

    arr[lo], arr[j] = arr[j], arr[lo]
    return j


def three_way_partition(arr, lo, hi): 
    """
    三路划分算法，将数组 arr[lo:hi+1] 划分为三个部分：
    - 小于 pivot 的元素： 位于 [lo, lt) 区间。
    - 等于 pivot 的元素： 位于 [lt, gt] 区间。
    - 大于 pivot 的元素： 位于 (gt, hi] 区间。
    
    Args:
        arr: 待划分的数组
        lo: 划分起始位置
        hi: 划分结束位置
    
    Returns:
        lt, gt: 两个指针，分别表示小于 pivot 部分的结束位置和大于 pivot 部分的起始位置
    """
    pivot = arr[lo]

    lt = lo
    gt = hi
    i = lo + 1

    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1

    return lt, gt


    
def quick_sort(nums, partition = hoare_partition2):

    def helper(nums, lo, hi):

        if lo < hi:
            p = partition(nums, lo, hi)
            # print(p, nums)            

            helper(nums, lo, p - 1)
            helper(nums, p + 1, hi)

    helper(nums, 0, len(nums) - 1)
    return nums


from test import test

test(quick_sort, [5,3,2,1])
test(quick_sort, [5,2,3,1])
test(quick_sort,  [5,1,1,2,0,0])
test(quick_sort,  [-1,2,-8,-10])
test(quick_sort,  [-2,3,-5])