# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        i = 0
        while head:
            a.append(head.val)
            head = head.next
        ans = ListNode()
        head = ans
        for i in a:
            if a.count(i) == 1:
                head.next = ListNode(i)
                head = head.next
        return ans.next

