# https://www.geeksforgeeks.org/what-is-linked-list/
# https://www.geeksforgeeks.org/data-structures/linked-list/singly-linked-list/
# https://www.geeksforgeeks.org/linked-list-set-2-inserting-a-node/
"""
Do it with Help of GFG:
Node class creation
Linked list class creation
insert at beginning
print Linked list
insert at last
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.nextPtr = None


class LinkedList:
    def __init__(self):
        self.head = None

    ## insert the new node at the beginning of the linked list
    def insertAtbeginning(self, new_data):
        ## create a new node for the new_data
        new_node = Node(new_data)
        ## insertion at the beginning of the linked list
        new_node.nextPtr = self.head
        self.head = new_node

    ## print the linked list
    def printLinkedList(self):
        temp = self.head
        while temp:
            print(str(temp.data) + " ", end=" ")
            temp = temp.nextPtr

    def insertAtend(self,new_data):
        new_node = Node(new_data)
        temp = self.head
        while temp.nextPtr:
            temp = temp.nextPtr
        temp.nextPtr= new_node
        print("-------",new_node.nextPtr)

    def inserAfterNode(self,prev_node,new_data):

        new_node = Node(new_data)
        new_node.nextPtr = prev_node.nextPtr
        prev_node.nextPtr = new_node




## Driver code
llist = LinkedList()
llist.insertAtbeginning(10)
llist.insertAtbeginning(20)
llist.insertAtbeginning(30)
llist.insertAtbeginning(40)
llist.insertAtbeginning(50)
llist.insertAtend(60)
llist.printLinkedList()

























