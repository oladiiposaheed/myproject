class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    #Add data at the beginning
    def insert_beginning(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    #Add data at the end
    def insert_end(self, data):
        newNode = Node(data)
        temp = self.head
        while temp.next != None:
            temp = temp.next
        newNode.next = temp.next
        temp.next = newNode
        newNode.next = None

    #Add data at any position except beginning and the end
    def insert_middle(self, data):
        newNode = Node(data)
        temp = self.head
        while temp.data != 40:
            temp = temp.next
        newNode.next = temp.next
        temp.next = newNode


    def display(self):
        if self.head is None:
            print('Linked List is Empty!')
        else:
            temp = self.head
            while temp != None:
                print(temp.data,'|',end=' ')
                temp = temp.next

L = SingleLinkedList()
n = Node(10)
L.head = n
n1 = Node(20)
L.head.next = n1
n2 = Node(30)
n1.next = n2
n3 = Node(40)
n2.next = n3
n4 = Node(50)
n3.next = n4

L.insert_beginning(5)
L.insert_beginning(3)

L.insert_end(60)
L.insert_end(70)
L.insert_end(86)

L.insert_middle(35)
L.insert_middle(18)
L.insert_middle(12)
L.insert_middle(-13)
L.display()