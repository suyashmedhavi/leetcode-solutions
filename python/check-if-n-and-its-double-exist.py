# https://leetcode.com/problems/check-if-n-and-its-double-exist

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i, v in enumerate(arr):
            try:
                if arr.index(v*2) not in [-1, i]:
                    return True
            except ValueError:
                continue
        return False

