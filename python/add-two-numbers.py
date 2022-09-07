# https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = l3 = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            carry, val = divmod(carry+(l1.val if l1 else 0)+(l2.val if l2 else 0), 10)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            l3.next = ListNode(val)
            l3 = l3.next
        return ans.next

