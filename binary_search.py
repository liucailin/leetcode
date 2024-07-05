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
    left, right = 0, len(arr)
    
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
    找到target要向左收缩区间
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



def binary_search_right(arr, target):
    """
    找到target要向右收缩区间
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


import test

fn = test.createAssert(binary_search)

fn(0, [1,2],1)
fn(1, [1,2],2)
fn(1, [1,1,2],1)
fn(1, [1,1,1,2],1)
fn(2, [1,1,1,1,2],1)
fn(2, [1,1,2,2],2)
fn(0, [1],1)
fn(-1, [],1)


fn = test.createAssert(binary_search_left)
fn(0, [1,2],1)
fn(1, [1,2],2)
fn(0, [1,1,2],1)
fn(2, [1,1,2,2],2)
fn(0, [1],1)
fn(-1, [],1)


fn = test.createAssert(binary_search_right)
fn(0, [1,2],1)
fn(1, [1,2],2)
fn(1, [1,1,2],1)
fn(3, [1,1,2,2],2)
fn(0, [1],1)
fn(-1, [],1)