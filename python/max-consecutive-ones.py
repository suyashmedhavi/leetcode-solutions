# https://leetcode.com/problems/max-consecutive-ones

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        curr = 0
        for i in nums:
            if i == 1:
                curr += 1
            else:
                ans, curr = max(ans, curr), 0
        return max(ans, curr)

