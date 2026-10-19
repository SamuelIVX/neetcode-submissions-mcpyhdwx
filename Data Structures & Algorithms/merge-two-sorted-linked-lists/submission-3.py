# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = temp = ListNode(-1)

        while list1 and list2: # While both LL are not empty
            if list1.val < list2.val: 
                temp.next = list1 
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next # Always increment the temp node
        
        # Either list can still have remaining nodes
        # as it is not guaranteed they are the same size
        temp.next = list1 or list2      

        # Return the head of the temp LL
        return dummy.next