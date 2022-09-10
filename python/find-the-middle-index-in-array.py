# https://leetcode.com/problems/find-the-middle-index-in-array

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        sumLeft, sumRight = 0, sum(nums)
        for i in range(len(nums)):
            if sumLeft == (sumRight-nums[i]): return i
            sumLeft, sumRight = sumLeft + nums[i], sumRight - nums[i]
        return -1

