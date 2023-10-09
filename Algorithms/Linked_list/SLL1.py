class Node:
    def __init__(self, data):
        self.data = data
        self.next = None #address of next Node

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert_begining(self, data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb

    def insert_end(self, data):
        ne = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ne

    #def insert_position(self, 4, 25):
    def insert_position(self, pos, data):
        np = Node(data)
        temp = self.head
        for i in range(pos - 1):
            temp = temp.next
        np.data = data
        np.next = temp.next
        temp.next = np

    def display(self):
        if self.head == None:
            print('Empty Linked List!')
        else:
            temp = self.head
            while temp:
                print(temp.data, '-->', end=' ')
                temp = temp.next

L = SingleLinkedList()
n = Node(10)
L.head = n   #address of the next Node
n1 = Node(20)
L.head.next = n1
n2 = Node(30)
n1.next = n2
n3 = Node(40)
n2.next = n3
n4 = Node(50)
n3.next = n4
L.insert_begining(5)
L.insert_begining(3)
L.insert_begining('Python')

L.insert_end(60)
L.insert_end(70)

L.insert_position(4, 25)
L.insert_position(6, 28)
L.insert_position(0, 2)
L.insert_position(7, 21)
L.display()