# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast, prev = head, head, None
        while fast and fast.next:
            slow, fast, prev = slow.next, fast.next.next, slow
        if prev:
            prev.next = slow.next
        else:
            head = None
        return head

