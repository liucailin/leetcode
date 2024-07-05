#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from typing import List

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)

        for word in strs:
            m[''.join(sorted(word))].append(word)

        return list(m.values())
# @lc code=end

