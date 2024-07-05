#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:

        record = set()

        def happy(n):
            if n == 1:
                return True
            elif n <= 3:
                return False
            else:
                numbers = []
                if n < 10:
                    numbers.append(n)
                else:
                    while n:
                        numbers.append(n % 10)
                        n = n // 10

                result = 0
                for num in numbers:
                    result += num * num

                if result in record:
                    return False
                
                record.add(result)

                return happy(result)
            
        return happy(n)

        

# print(Solution().isHappy(7))
# print(Solution().isHappy(8))
# print(Solution().isHappy(9))
# print(Solution().isHappy(19))
# print(Solution().isHappy(2))
# @lc code=end

