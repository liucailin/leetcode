#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1

        carry = 0
        ans = []

        while i >= 0 or j >= 0:
            sum = carry
            if i >= 0 : sum += ord(a[i]) - ord('0')
            if j >= 0 : sum += ord(b[j]) - ord('0')

            ans.append(str(sum % 2))
            carry = sum // 2
            
            i -= 1
            j -= 1

        if carry == 1:
            ans.append('1')

        ans.reverse()
        return ''.join(ans)

        
# @lc code=end



# addBinary = Solution().addBinary

# print(addBinary("1010", "1011"))
# print(addBinary("11", "1"))