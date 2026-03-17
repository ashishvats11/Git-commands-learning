# In this we will be learning about the Linkedlist

# Creating a class for creating a node in python
class Node:
    def __init__(self, data = None, next = None):           
        self.data = data 
        self.next = next

class singlyLinkedList:
    def __init__(self,head = None):
        self.head = head
    
    # add node at the end 
    def insertAtEnd(self,value):
        node = Node(value)
        
        if self.head != None:
            curr_node = self.head
            while curr_node.next !=None:
                curr_node = curr_node.next
            curr_node.next = node
            node.next = None
        else:
            self.head = node

    # add node at the begining
    def insertAtBegining(self, value):
        node = Node(value)
        if self.head != None:
            node.next = self.head
            self.head = node
        else:
            self.head = node
    
    # add node in between - add after the value defined
    def insertInBetween(self, value, x):
        node = Node(value)
        if self.head!=None:
            curr_node = self.head
            while(curr_node.data != x and curr_node!=None):
                curr_node = curr_node.next
            node.next = curr_node.next
            curr_node.next = node
            
        else:
            self.head = node
        return

    # Delete a node from the linkedlist
    def delete_LL(self, value):
        if (self.head!=None):
            curr = self.head
            prev = None 
            while (curr != None and curr.data!=value):
                prev = curr
                curr = curr.next
            prev.next = curr.next
            # curr.next = None  not necessary
        else:
            print("The Linked list is empty")
        

    # Print the Linked list
    def print_linkedlist (self):
        curr_node = self.head
        while (curr_node.next != None):
            print(curr_node.data, end = ' ---> ')
            curr_node = curr_node.next
        print(curr_node.data) 

  



LL_1 = singlyLinkedList()
LL_1.insertAtEnd(10)
LL_1.insertAtEnd(20)
LL_1.insertAtEnd(30)
LL_1.insertAtEnd(40)
LL_1.insertAtBegining(100)
LL_1.insertInBetween(50,20)
LL_1.delete_LL(40)
LL_1.print_linkedlist()

 