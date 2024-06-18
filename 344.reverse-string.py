#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        slow, fast = 0, len(s) - 1
        while slow < fast:
            s[slow], s[fast] = s[fast], s[slow]
            slow += 1
            fast -= 1
        
# @lc code=end

