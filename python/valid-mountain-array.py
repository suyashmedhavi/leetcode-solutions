# https://leetcode.com/problems/valid-mountain-array

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: return False
        increasing, decreasing = False, False
        i = 1
        while i < len(arr) and arr[i] > arr[i-1]:
            i += 1
            increasing = True
        while i < len(arr) and arr[i] < arr[i-1]:
            i += 1
            decreasing = True
        return (i == len(arr) and increasing and decreasing)

