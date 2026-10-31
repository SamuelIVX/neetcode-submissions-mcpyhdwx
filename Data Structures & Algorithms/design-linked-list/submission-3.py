class ListNode():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = ListNode()

    def get(self, index: int) -> int:
        if index >= self.size or index < 0: return - 1

        curr = self.head.next
        while index:
            curr = curr.next
            index -= 1
        
        return curr.val

    def addAtHead(self, val: int) -> None:
        curr = self.head
        next_node = curr.next
        new_node = ListNode(val)

        curr.next = new_node
        new_node.next = next_node

        self.size += 1

    def addAtTail(self, val: int) -> None:
        curr = self.head
        new_node = ListNode(val)

        while curr.next:
            curr = curr.next
        
        curr.next = new_node
        new_node.next = None

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size or index < 0: return

        curr = self.head
        new_node = ListNode(val)

        while index:
            curr = curr.next
            index -= 1
        
        next_node = curr.next
        curr.next = new_node
        new_node.next = next_node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0: return

        curr = self.head
        while index:
            curr = curr.next
            index -= 1

        next_node = curr.next.next
        curr.next = next_node

        self.size -=1 

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)