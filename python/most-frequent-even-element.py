# https://leetcode.com/problems/most-frequent-even-element

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq = -1
        ans = -1
        for i in sorted(set(nums)):
            if i%2 == 0 and nums.count(i) > freq:
                freq = nums.count(i)
                ans = i
        return ans

