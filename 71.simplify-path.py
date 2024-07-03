#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        n = len(path)
        i, j = 0, 0

        for j in range(1, n):
            c = path[j]

            p = None
            if c == '/':
                p = path[i+1:j]
                i = j
            elif j == n - 1:
                p = path[i+1:]

            
            if p == '..':
                if stack:
                    stack.pop()
            elif p and p != '.':
                stack.append(p)
            
        
        return '/' + '/'.join(stack)
# @lc code=end

# import test
# fn = test.createTest(Solution().simplifyPath)

# fn("/a//b////c/d//././/..")
# fn("/a/../../b/../c//.//")
# fn("/home/")
# fn("/home//foo/")
# fn("/home/user/Documents/../Pictures")
# fn("/../")
# fn("/.../a/../b/c/../d/./")
    

# 直接用split
def simplifyPath(path):
    places = [p for p in path.split("/") if p!="." and p!=""]
    stack = []
    for p in places:
        if p == "..":
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(p)
    return "/" + "/".join(stack)