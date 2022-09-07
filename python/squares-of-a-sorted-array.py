# https://leetcode.com/problems/squares-of-a-sorted-array

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        i, j = 0, len(nums)-1
        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                ans.append(nums[i]*nums[i])
                i += 1
            else:
                ans.append(nums[j]*nums[j])
                j -= 1
        return reversed(ans)

