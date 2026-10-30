class ListNode:
    def __init__(self, val = 0, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = ListNode()
        self.tail = ListNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        if index >= self.size or index < 0: return -1

        curr = self.head.next

        while index:
            curr = curr.next
            index -= 1

        return curr.val

    def addAtHead(self, val: int) -> None:
        # Optimization Technique: Reuse addAtIndex()!
        self.addAtIndex(0, val)

        # # 1. Create the new node
        # new_node = ListNode(val)
        
        # # 2. Set up the new node's outgoing links
        # new_node.next = self.head.next
        # new_node.prev = self.head
        
        # # 3. Update the surrounding nodes' links to point to the new node
        # self.head.next.prev = new_node
        # self.head.next = new_node

        # # 4. Increment the size of the list
        # self.size += 1

    def addAtTail(self, val: int) -> None:
        # Optimization Technique: Reuse addAtIndex()!
        self.addAtIndex(self.size, val)

        # # 1. Save references to the dummy tail and the node currently before it
        # temp_tail = self.tail
        # temp_prev = self.tail.prev

        # # 2. Create the new node
        # new_node = ListNode(val)

        # # 3. Connect the dummy tail and the new node
        # temp_tail.prev = new_node
        # new_node.next = temp_tail

        # # 4. Connect the old previous node and the new node
        # temp_prev.next = new_node
        # new_node.prev = temp_prev

        # # 5. Increment the size of the list
        # self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        # 1. If index is invalid, we can't add a new node
        if index > self.size or index < 0: return 

        curr = self.head

        # 2. The current node will be the prev node
        while index:
            curr = curr.next
            index -= 1

        new_node = ListNode(val)
        next_node = curr.next

        # 3. Add the new node in the list
        curr.next = new_node
        new_node.prev = curr

        new_node.next = next_node
        next_node.prev = new_node

        # 4. Increment the size of the list
        self.size += 1
        
    def deleteAtIndex(self, index: int) -> None:
        # There is no index-th node to delete in the list
        if index >= self.size or index < 0: return

        # Remove the index-th node in the list
        curr = self.head.next
        while index:
            curr = curr.next
            index -= 1
        
        prev_node = curr.prev
        next_node = curr.next

        prev_node.next = next_node
        next_node.prev = prev_node

        # Decrement the size of the list
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)