def binary_search(arr, target):
    """
    搜索区间 [left, right]
    循环终止条件 left == right + 1
    循环终止 []
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# 不要用这个
def binary_search2(arr, target):
    """
    搜索区间 [left, right)
    循环终止条件 left == right
    循环终止 [left]
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left if arr and arr[left] == target else -1


def binary_search_left(arr, target):
    """
    循环不变式
    在每次迭代开始时，我们希望保持以下不变式：

    left 左侧的元素都小于 target。
    right 右侧的元素都大于或等于 target。
    目标值 target 的最左侧位置在 [left, right] 区间内。
    分析步骤
    初始化：

    left = 0，指向数组的开头。
    right = len(arr) - 1，指向数组的末尾。
    循环保持：

    在每次迭代中，计算 mid = (left + right) // 2。
    根据 arr[mid] 与 target 的比较调整 left 和 right 的值：
    如果 arr[mid] < target，说明目标值在 mid 的右侧，因此更新 left = mid + 1。
    如果 arr[mid] >= target，说明目标值在 mid 的左侧或正好是 mid，因此更新 right = mid - 1。
    终止条件：

    当 left > right 时，循环终止。此时，如果存在目标值 target，left 就是目标值的最左侧位置。
    如果数组中不存在目标值 target，则 left 将指向第一个大于 target 的元素位置，或者数组的长度，因此需要判断 left 是否等于数组长度来确定是否找到目标值。
    返回结果：

    如果找到目标值 target，返回 left。
    如果未找到目标值 target，返回 -1。
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if left == len(arr): return -1
    
    return left if arr[left] == target else -1



def binary_search_left2(arr, target):
    """
    循环不变式
    在每次迭代开始时，我们希望保持以下不变式：

    left 左侧的元素都小于 target 或者等于 target。
    right 右侧的元素都大于 target。
    目标值 target 的最左侧位置在 [left, right) 区间内。
    分析步骤
    初始化：

    left = 0，指向数组的开头。
    right = len(nums)，指向数组的末尾。
    循环保持：

    在每次迭代中，计算 mid = (left + right) // 2。
    根据 nums[mid] 与 target 的比较调整 left 和 right 的值：
    如果 nums[mid] >= target，则目标值 target 在 mid 的左侧或正好是 mid。
    因此更新 right = mid，缩小搜索范围到 [left, mid)。
    如果 nums[mid] < target，则目标值 target 在 mid 的右侧。
    因此更新 left = mid + 1，缩小搜索范围到 [mid + 1, right)。
    终止条件：

    当 left 等于 right 时，循环终止。
    如果存在目标值 target，left 就是目标值的最左侧位置。
    如果数组中不存在目标值 target，则 left 将指向第一个大于 target 的元素位置，或者数组的长度。
    返回结果：

    返回 left，即为目标值 target 的最左侧位置。
    """
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid
        else:
            left = mid + 1
    
    return left


def binary_search_right(arr, target):
    """
    找到target要收缩左侧边界
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    if right < 0: return -1

    return right if arr[right] == target else -1 


def binary_search_right2(arr, target):
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    
    return left - 1


import test

fn = test.createAssert(binary_search2)

fn(0, [1,2],1)
fn(9, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],10)
fn(1, [1,2],2)
fn(1, [1,1,2],1)
fn(1, [1,1,1,2],1)
fn(2, [1,1,1,1,2],1)
fn(2, [1,1,2,2],2)
fn(0, [1],1)
fn(-1, [],1)


fn = test.createAssert(binary_search_left2)
fn(4, [1,2,3,4],5)
fn(0, [1,2,3,4],0)
fn(0, [1,2],1)
fn(1, [1,2],2)
fn(0, [1,1,2],1)
fn(2, [1,1,2,2],2)
fn(0, [1],1)
fn(0, [],1)


fn = test.createAssert(binary_search_right)
fn(4, [1,2,3,4],5)
fn(0, [1,2,3,4],0)
fn(0, [1,2],1)
fn(1, [1,2],2)
fn(1, [1,1,2],1)
fn(3, [1,1,2,2],2)
fn(0, [1],1)
fn(-1, [],1)