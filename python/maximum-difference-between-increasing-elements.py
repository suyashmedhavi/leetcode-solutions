# https://leetcode.com/problems/maximum-difference-between-increasing-elements

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans, minNum = -1, nums[0]
        for i in range(1, len(nums)):
            ans = max(ans, nums[i]-minNum)
            minNum = min(minNum, nums[i])
        return ans if ans != 0 else -1

