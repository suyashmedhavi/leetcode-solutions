# https://leetcode.com/problems/remove-element

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while nums.count(val) > 0:
            nums.remove(val)

