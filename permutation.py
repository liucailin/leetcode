from functools import reduce

def permute(nums):
    if not nums:
        return [[]]
    else:
        result = []
        for i, n in enumerate(nums):
            remaining = nums[:i] + nums[i+1:]
            for p in permute(remaining):
                result.append([n] + p)
        return result

def permute1(nums):
    """
    递归拆分：对于 nums 中的每个元素 n, 递归调用 permute1 生成剩余元素的所有排列。
    组合排列：将元素 n 添加到每个生成的排列 p 的前面，形成新的排列。
    基准情况：当 nums 为空时，返回 [[]] 表示只有一种空排列。
    """
    return [[n] + p
            for i, n in enumerate(nums)
            for p in permute1(nums[:i] + nums[i+1:])] or [[]]


def permute2(nums):
    """
    递归拆分：将列表 nums 拆分为第一个元素 nums[0] 和剩余部分 nums[1:]。
    生成子排列：递归调用 permute2 生成剩余部分的所有排列。
    插入元素：将 nums[0] 插入到每个生成的排列 p 的所有可能位置。
    基准情况：当 nums 为空时，返回 [[]] 表示只有一种空排列。
    """
    return nums and [p[:i] + [nums[0]] + p[i:]
                     for p in permute2(nums[1:])
                     for i in range(len(nums))] or [[]]



def permute3(nums):
    return reduce(lambda P, n: [p[:i] + [n] + p[i:]
                                for p in P for i in range(len(p)+1)],
                  nums, [[]])


def permute4(nums):
    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]  # 交换
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]  # 撤销交换
    
    result = []
    backtrack(0)
    return result


def permute5(nums):
    def backtrack(path, used):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            path.append(nums[i])
            used[i] = True
            backtrack(path, used)
            path.pop()
            used[i] = False
    
    result = []
    used = [False] * len(nums)
    backtrack([], used)
    return result


def gen_perms(seq):
    """
    使用生成器，适合处理大量数据，惰性求值
    """
    if not seq:
        yield []
    else:
        for s in gen_perms(seq[1:]):
            for i in range(len(seq)):
                yield s[:i] + [seq[0]] + s[i:]


input = [1,2,3]

print(permute1(input))
print(permute2(input))

print(list(gen_perms("abc"))) 
