# https://leetcode.com/problems/add-to-array-form-of-integer

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        ans, i = [], len(num)-1
        while k>0 or i>=0:
            k, rem = divmod(k+(num[i] if i>=0 else 0), 10)
            ans.append(rem)
            i -= 1
        return reversed(ans)

