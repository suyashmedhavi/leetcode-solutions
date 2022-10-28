# https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        head = ans
        while list1 and list2:
            if list1.val < list2.val:
                head.next = ListNode(list1.val)
                head, list1 = head.next, list1.next
            else:
                head.next = ListNode(list2.val)
                head, list2 = head.next, list2.next
        if list1: head.next = list1
        if list2: head.next = list2
        return ans.next

