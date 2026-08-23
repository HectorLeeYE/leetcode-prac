class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def get(self, index: int) -> int:
        # Traverse the list
        if index < 0 or index >= self.size:
            return -1

        curr = self.head
        for i in range(index):
            curr = curr.next
        
        return curr.val


    def addAtHead(self, val: int) -> None:
        new_node = Node(val)        # Create node
        new_node.next = self.head
        self.head = new_node
        
        if self.size == 0:
            self.tail = new_node

        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.addAtHead(val)
            return 

        new_node = Node(val)

        self.tail.next = new_node
        self.tail = new_node
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.size:
            self.addAtTail(val)
            return
        elif index > self.size or index < 0: 
            return 
        elif index == 0:
            self.addAtHead(val)
            return

        new_node = Node(val)

        curr = self.head
        for i in range(index-1):
            # Traverse the list to node before
            curr = curr.next
        new_node.next = curr.next       # Add right
        curr.next = new_node            # Add left

        self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0:
            return None
        
        if index == 0:
            self.head = self.head.next
            self.size -= 1

            if self.size == 0:
                self.tail=None

            return
        
        curr = self.head
        for i in range(index-1):
            curr = curr.next
        
        curr.next = curr.next.next
        if index == self.size -1:
            self.tail = curr

        self.size -= 1




# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)