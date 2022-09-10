# https://leetcode.com/problems/word-pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_arr = s.split()
        return len(pattern) == len(s_arr) and len(set(zip(pattern, s_arr))) == len(set(pattern)) == len(set(s_arr))

