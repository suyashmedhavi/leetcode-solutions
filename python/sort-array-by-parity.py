# https://leetcode.com/problems/sort-array-by-parity

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i, j, ans = 0, len(nums)-1, [0] * len(nums)
        for v in nums:
            if v % 2 == 0: ans[i], i = v, i+1
            else: ans[j], j = v, j-1
        return ans

