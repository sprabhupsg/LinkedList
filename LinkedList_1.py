# Create a Node class to create a node
# Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create a LinkedList class
# Node -> Node -> None
class LinkedList:
    # None
    # head
    def __init__(self):
        self.head = None

    # Method to add a node at the beginning of the LL
    # new_node -> Node -> Node -> Node -> None
    # head
    def insertAtBegin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    # Method to add a node at the end of LL
    # Node -> Node -> Node -> new
    # head
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    # Print the size of the linked list
    def sizeOfLL(self):
        size = 0
        current_node = self.head
        while current_node:
            size += 1
            current_node = current_node.next
        return size

    # Print the linked list
    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end="->")
            current_node = current_node.next

    # Get the head node
    def getHead(self):
        return self.head

    # Print the linked list in reverse
    def printRevLL(self, current_node):
        if current_node == None:
            return
        self.printRevLL(current_node.next)
        print(current_node.data, end="->")



# create a new linked list
llist = LinkedList()

# add nodes to the linked list
llist.insertAtEnd('b')
llist.insertAtEnd('c')
llist.insertAtBegin('a')
llist.insertAtEnd('d')

# print the linked list
print("Node Data:")
llist.printLL()

# print the linked list
print("\nSize of linked list:", llist.sizeOfLL())

#head node
my_head = llist.getHead()

# print the linked list in reverse
print("Node Data in reverse:")
llist.printRevLL(my_head)


'''
#Output
Node Data:
a->b->c->d->
Size of linked list: 4
Node Data in reverse:
d->c->b->a->
'''




