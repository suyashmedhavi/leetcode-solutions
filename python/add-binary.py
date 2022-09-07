# https://leetcode.com/problems/add-binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j, carry = len(a)-1, len(b)-1, 0
        ans = ""
        while i>=0 or j>=0:
            sum = carry
            if i>=0:
                sum += int(a[i])
            if j>=0:
                sum += int(b[j])
            carry = 1 if sum>1 else 0
            sum = sum%2
            ans = str(sum) + ans
            i, j = i-1, j-1
        if carry>0:
            ans = "1"+ans
        return ans

