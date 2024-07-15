#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#
"""
1. 环形数组的迭代技巧

"""

# @lc code=start
from typing import List


def canCompleteCircuit_Greedy(gas: List[int], cost: List[int]) -> int:
    """
    贪心
    总加油量 >= 总耗油量 才有解
    """
    n = len(gas)
    cursum = totalsum = 0
    start_index = 0
    for i in range(n):
        diff = gas[i] - cost[i]
        cursum += diff
        totalsum += diff

        if cursum < 0:
            start_index = i + 1
            cursum = 0
    
    return start_index if totalsum >= 0 else -1



def canCompleteCircuit_Opt(gas: List[int], cost: List[int]) -> int:
    """
    基于暴力枚举优化迭代，如果不能达到，直接从不能达到的index开始
    O(2n)  O(n)
    """
    n = len(gas)
    i = 0
    while i < n:
        tank = 0
        count = 0
        while count < n:
            j = (i + count) % n
            tank += gas[j]
            tank -= cost[j]
            if tank < 0:
                break
            count += 1

        if count == n:
            return i
        
        i += count + 1
        
    return -1


def canCompleteCircuit_Brute(gas: List[int], cost: List[int]) -> int:
    """
    暴力枚举 O(n^2)
    """
    n = len(gas)
    for i in range(n):
        tank = 0
        complete = True
        for j in range(n):
            k = (i + j) % n
            tank += gas[k]
            tank -= cost[k]
            if tank < 0:
                complete = False
                break

        if complete:
            return i
        
    return -1


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        return canCompleteCircuit_Greedy(gas, cost)

# @lc code=end

canCompleteCircuit = canCompleteCircuit_Greedy
test = lambda gas, cost: print(gas, cost, canCompleteCircuit(gas, cost))

test([5,8,2,8], [6,5,6,6]) # 3
test([1,2,3,4,5], [3,4,5,1,2]) # 3
test([2,3,4], [3,4,3]) # -1