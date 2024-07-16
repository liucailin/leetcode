#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
# @lc code=start

from typing import List

def brute(s: str, wordDict: List[str], memo = {}):
    if s in memo:
        return memo[s]
    if s in wordDict:
        return True
    for i in range(1, len(s)):
        if s[:i] in wordDict and brute(s[i:], wordDict, memo):
            memo[s[i:]] = True
            return True
    memo[s] = False
    return False

def brute_memo(s: str, wordDict: List[str]):

    import functools
    @functools.lru_cache(None)
    def dfs(s):
        if s in wordDict:
            return True
        for i in range(1, len(s)):
            if s[:i] in wordDict and dfs(s[i:]):
                return True

        return False
    
    return dfs(s)


def brute_memo2(s: str, wordDict: List[str]):

    memo = {}

    def dfs(s):
        if s in memo:
            return memo[s]
        if s in wordDict:
            return True
        for i in range(1, len(s)):
            if s[:i] in wordDict and dfs(s[i:]):
                memo[s[i:]] = True
                return True

        memo[s] = False
        return False
    
    return dfs(s)


def dp_method(s: str, wordDict: List[str]):
    n = len(s)
    dp = [False]*(n+1)
    dp[0] = True
    for i in range(n):
        for j in range(i+1,n+1):
            if(dp[i] and (s[i:j] in wordDict)):
                dp[j]=True
    return dp[-1]




class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return dp_method(s, wordDict)
        



# @lc code=end

wordBreak = brute
def test(s, t): return print(s, t, wordBreak(s, t))


test("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", [
     "a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"])
test("leetcode", ["leet", "code"])
test("applepenapple", ["apple", "pen"])
test("catsandog", ["cats", "dog", "sand", "and", "cat"])
test("aaaaaaa", ["aaaa","aaa"])