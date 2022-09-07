# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result = 0
        last = ""
        for c in reversed(s):
            if c == "I" and (last == "V" or last == "X"):
                result -= dict[c]
            elif c == "X" and (last == "L" or last == "C"):
                result -= dict[c]
            elif c == "C" and (last == "D" or last == "M"):
                result -= dict[c]
            else:
                result += dict[c]
            last = c
        return result

