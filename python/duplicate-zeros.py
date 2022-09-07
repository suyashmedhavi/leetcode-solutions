# https://leetcode.com/problems/duplicate-zeros

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i, l = 0, len(arr)
        while i < l:
            if arr[i] == 0:
                j = len(arr)-1
                while j > i:
                    arr[j] = arr[j-1]
                    j -= 1
                i += 1
            i += 1

