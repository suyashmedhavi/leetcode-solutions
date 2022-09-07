# https://leetcode.com/problems/ransom-note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = list(ransomNote)
        b = list(magazine)
        for c in a:
            if c in b:
                b.remove(c)
            else:
                return False
        return True

