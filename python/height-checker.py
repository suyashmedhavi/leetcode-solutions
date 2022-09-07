# https://leetcode.com/problems/height-checker

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count, expected = 0, sorted(heights)
        for i in range(len(heights)):
            if heights[i] != expected[i]: count += 1
        return count

