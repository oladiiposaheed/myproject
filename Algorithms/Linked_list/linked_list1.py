class Node:
    def __init__(self, data):
        '''Fist Node has data but no next i.e no collection to the next node'''
        self.data = data
        self.next = None # Address of the next node

class SingleLinkedList:
    def __init__(self):
        self.head = None

    '''To display the node in the SLL'''
    def display(self):
        if self.head is None:
            print('Single Linked List is Empty')

        else:
            temp = self.head
            while temp:
                print(temp.data, '-->', end=' ')
                temp = temp.next

L = SingleLinkedList()
#L.display()
#Create object for the Node
n = Node(10)  #1st Node with data = 10 next = None
L.head = n   #address of next Node
n1 = Node(20)
L.head.next = n1  #2nd Node with data = 10 next =
n2 = Node(30)
 #L.head.next.next = n2
n1.next = n2      #2nd Node with data
n3 = Node(50)
#L.head.next.next.next = n3
n2.next = n3    #2nd Node with data
L.display()