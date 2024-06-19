#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#

# @lc code=start
from typing import List



class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0
        j = 0
        k = 0
        for i in range(1, len(chars) + 1):
           if i == len(chars) or chars[i] != chars[j]:
                n = i - j
                if n > 1:
                    for s in str(n):
                        k += 1
                        chars[k] = s
                k += 1
                if i < len(chars):
                    chars[k] = chars[i]
                j = i

        return k

        
# @lc code=end

# from test import test

# test(Solution().compress, ["a","a","b","b","c","c","c"])
# test(Solution().compress, ["a"])
# test(Solution().compress, ["a","b","b","b","b","b","b","b","b","b","b","b","b"])