# https://leetcode.com/problems/insert-interval

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left = [i for i in intervals if i[1]<newInterval[0]]
        right = [i for i in intervals if i[0]>newInterval[1]]
        if left + right != intervals:
            new = [[min(intervals[len(left)][0], newInterval[0]), max(intervals[len(intervals)-len(right)-1][1], newInterval[1])]]
            return left + new + right
        return left + [newInterval] + right

