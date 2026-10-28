# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        root = dummy = ListNode(0, head)
        temp = head

        while temp:
            length += 1
            temp = temp.next

        length -= n
        temp = head

        while length:
            dummy = dummy.next
            temp = temp.next
            length -= 1
        
        dummy.next = temp.next

        return root.next



























        # length = 0
        # root = dummy = ListNode(0,head)
        # temp = head

        # while temp:
        #     length += 1
        #     temp = temp.next

        # length -= n
        # temp = head

        # while length:
        #     dummy = dummy.next
        #     temp = temp.next
        #     length -= 1
        
        # dummy.next = temp.next

        # return root.next