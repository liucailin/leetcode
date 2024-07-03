#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        window = {}

        for c in t:
            need[c] = need.get(c, 0) + 1

        left, right = 0, 0
        valid = 0
        start, min_len = 0, float('inf')

        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1


            while valid == len(need):
                if right - left < min_len:
                    min_len = right - left
                    start = left
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return s[start: start + min_len] if min_len != float('inf') else ''
        
# @lc code=end

