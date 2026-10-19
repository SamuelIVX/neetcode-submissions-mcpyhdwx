# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ret_list = ListNode();
        root = ret_list;
        while list1 != None or list2 != None:
            if list1 == None:
                ret_list.next = list2
                list2 = list2.next
                ret_list = ret_list.next
                continue
            elif list2 == None:
                ret_list.next = list1
                list1 = list1.next
                ret_list = ret_list.next
                continue

            if(list1.val < list2.val):
                ret_list.next = list1
                list1 = list1.next
            else:
                ret_list.next = list2
                list2 = list2.next
            ret_list = ret_list.next


        return root.next