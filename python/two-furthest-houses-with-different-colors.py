# https://leetcode.com/problems/two-furthest-houses-with-different-colors

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = 0
        for i, v in enumerate(colors):
            if v != colors[0]: ans = max(ans, i)
            if v != colors[-1]: ans = max(ans, len(colors)-i-1)
        return ans

