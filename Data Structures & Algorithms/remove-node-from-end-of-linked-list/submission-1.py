# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp = head
        root = dummy = ListNode(0, head)

        while temp:
            length += 1
            temp = temp.next
        
        temp = head
        length -= n

        while length:
            dummy = dummy.next
            temp = temp.next
            length -= 1

        dummy.next = temp.next

        return root.next