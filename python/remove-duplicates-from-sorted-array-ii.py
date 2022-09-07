# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        copy = nums[:]
        for i in nums:
            while copy.count(i) > 2:
                copy.remove(i)
        nums[:] = copy

