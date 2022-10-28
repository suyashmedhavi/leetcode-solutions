# https://leetcode.com/problems/reorder-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        curr, i, j, k = head, 0, len(arr)-1, 0
        while curr:
            if k%2 == 0:
                curr.val = arr[i]
                i += 1
            else:
                curr.val = arr[j]
                j -= 1
            k += 1
            curr = curr.next
        return head

