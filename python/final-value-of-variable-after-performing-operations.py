# https://leetcode.com/problems/final-value-of-variable-after-performing-operations

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        mapping = {"--X":-1, "X--":-1, "++X":1, "X++":1}
        ans = 0
        for opr in operations:
            ans += mapping[opr]
        return ans

