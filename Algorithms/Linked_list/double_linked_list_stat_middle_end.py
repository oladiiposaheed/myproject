class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print('Empty Double Linked List')
        else:
            temp = self.head
            while temp:
                print(temp.data, '|', end=' ')
                temp = temp.next

    def insert_start(self, data):
        newNode = Node(data)
        temp = self.head
        temp.prev = newNode
        newNode.next = temp
        self.head = newNode

    def insert_end(self, data):
        newNode = Node(data)
        temp = self.head
        while temp.next != None:
            temp = temp.next
        newNode.prev = temp
        temp.next = newNode
        newNode.next = None

    def insert_position(self, pos, data):
        newNode = Node(data)
        temp = self.head
        for i in range(1, pos - 1):
            temp = temp.next
        newNode.prev = temp
        newNode.next = temp.next
        temp.next = newNode
        temp.next.prev = newNode



L = DLL()
n1 = Node(10)
L.head = n1
n2 = Node(20)
n2.prev = n1
n1.next = n2
n3 = Node(30)
n3.prev = n2
n2.next = n3
n4 = Node(40)
n4.prev = n3
n3.next = n4
n5 = Node(50)
n5.prev = n4
n4.next = n5
n6 = Node(60)
n6.prev = n5
n5.next = n6

L.insert_start(6)
L.insert_start(2)

L.insert_end(70)
L.insert_end(85)
L.insert_end(90)
L.insert_end(100)

L.insert_position(3, 35)
L.insert_position(1, -10)
L.insert_position(1, -3)
L.display()