# https://leetcode.com/problems/optimal-partition-of-string

class Solution:
    def partitionString(self, s: str) -> int:
        ans = 1
        seen = set()
        for i in s:
            if i in seen:
                seen.clear()
                ans += 1
            seen.add(i)
        return ans

