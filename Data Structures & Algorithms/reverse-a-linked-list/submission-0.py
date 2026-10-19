# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            temp = curr.next # Points to the next node
            curr.next = prev # Points the next node to the prev node
            prev = curr # Point the prev node to the curr node
            curr = temp # Make sure the rest of the linked-list is not lost
        
        return prev