#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#


def hIndex_CountingSort(citations):
    """
    计数排序
    最大值是n，因为h-index不可能超过paper数量
    count[i]表示引用次数为i的paper数量

    """
    n = len(citations)
    count = [0] * (n + 1)
    for c in citations:
        if c >= n:
            count[n] += 1
        else:
            count[c] += 1

    sum = 0
    for h in range(n, -1, -1):
        sum += count[h]
        if sum >= h:
            return h
        
    return 0

# @lc code=start
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        h = 0
        for i in range(len(citations) - 1, -1, -1):
            if citations[i] > h:
                h += 1
        return h
        
# @lc code=end

hIndex = hIndex_CountingSort
test = lambda nums: print(nums, hIndex(nums))

test([3,0,6,1,5])
test([1,3,1])