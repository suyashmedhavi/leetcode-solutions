# https://leetcode.com/problems/reverse-linked-list-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        a = []
        i = 0
        while head:
            a.append(head.val)
            head = head.next
        ans = ListNode()
        head = ans
        a = a[:left-1]+list(reversed(a[left-1:right]))+a[right:]
        for i in a:
            head.next = ListNode(i)
            head = head.next
        return ans.next

