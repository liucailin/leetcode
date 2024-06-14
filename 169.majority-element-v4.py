# 摩尔投票算法/多数投票算法（Boyer-Moore Voting Algorithm）


from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 第一遍遍历找出候选者
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        # 第二遍遍历验证候选者是多数元素
        count = 0
        for num in nums:
            if num == candidate:
                count += 1
        
        if count > len(nums) // 2:
            return candidate
        raise ValueError("No majority element found")