class Node:
    # A doubly-linked node.
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    # A doubly-linked list.
    def __init__(self):
        # Create an empty list.
        self.tail = None
        self.head = None
        self.count = 0

    def iter(self):
        # Iterate through the list.
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val


    def size(self):
        # Returns the number of elements in the list
        return self.count


    def addFirst(self, data):
        # Add a node at the front of the list
        self.count += 1
        newNode = Node(data)
        
        if self.head :
            self.head.prev = newNode
            newNode.next = self.head
        else:
            self.head = newNode
            self.tail = newNode #now sets tail to equal newNode as well

    def addLast(self, data):
        #Add a node at the end of the list
        self.count += 1
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

    def addAtIndex(self, data, index):
        if (index > self.count) and (index < 0):
            return
        if (index == self.count):
            self.addLast(data)
            return
        if index == 0:
            self.addFirst(data)
            return
        curr = self.head
        prev = self.head
        for n in range(index):
            prev = curr
            curr = curr.next
        node = Node(data)
        prev.next = node
        node.prev = prev
        node.next = curr
        curr.prev = node
        self.count += 1
        return

    def indexOf(self, data):
        # Search through the list. Return the index position if data is found, otherwise return -1
        curr = self.head
        ind = 0
        while curr.next != None:
            if(curr.data == data):
                return ind
            else:
                ind += 1
                curr = curr.next
        return -1


    def replace(self, data, temp):
        index = self.indexOf(temp)
        
        current = self.head
        for n in range(index):
            current = current.next
        current.data = data
        
        # node = Node(data)
        # if (index > (self.count - 1)):
        #     return
        # if (index == (self.count -1)):
        #     self.addLast(data)
        #     return
        # if index == 0:
        #     self.addFirst(data)
        #     return
        # curr = self.head
        # prev = self.head
        # for n in range(index):
        #     prev = curr
        #     curr = curr.next        
        # prev.next = node
        # node.prev = prev
        # node.next = curr
        # curr.prev = node
        # next = curr.next
        # curr = curr.prev
        # curr.next = next
        # return

    def add(self, data) -> None:
        # Append an item to the end of the list
        self.addLast(data)

    def clear(self) -> None:
        # Remove all of the items from the list
        self.head = None
        self.tail = None
        self.count = 0

    def deleteAtIndex(self, index) -> None:
        # Delete the node at the index-th in the linked list, if the index is valid.

        if (index > (self.count-1)):
            return
            
        curr = self.head
        prev = self.head

        for n in range(index):
            prev = curr
            curr = curr.next
            
        prev.next = curr.next
        curr.prev = prev
        self.count -= 1

        if (curr == self.head):
            self.head = curr.next
            curr.prev = None
        elif (curr == self.tail):
            prev.next = None
            self.tail = prev       

        return

    def delete(self, data) -> None:
        # Delete a node from the list who's value matches the supplied value
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.tail:
                    prev.next = None
                    self.tail = prev
                elif current == self.head:
                    current.next.prev = None
                    self.head = current.next
                else:
                    prev.next = current.next
                    current.next = prev
                self.count -= 1
                return
            prev = current
            current = current.next

    def __getitem__(self, index):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index, value):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        current.data = value

    def __str__(self):
        myStr = ""
        for node in self.iter():
             myStr += str(node)+ " "
        return myStr
    
items = DoublyLinkedList()
items.addFirst("May")
items.add("the")
items.add("force")
items.add("be")
items.add("with")
items.add("you")
items.add("!")
print(items)
print(items.indexOf("with"))
items.addAtIndex('all', 6)
items.replace('us', 'you')
print(items)