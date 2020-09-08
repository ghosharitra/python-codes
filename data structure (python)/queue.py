class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None

    def display(self):
        print("Queue: ", end="")
        if self.head != None:
            p = self.head
            while p.next != None:
                print(p.data, "-> ", end="")
                p = p.next
            print(p.data)
        else:
            print("EMPTY")

    def push(self):
        new = Node(input())

        if (self.head == None):
            self.head = new
        else:
            p = self.head
            while p.next != None:
                p = p.next
            p.next = new

    def pop(self):
        if self.head != None:
            x = self.head.data
            self.head = self.head.next
            print("popped element: ", x)
        else:
            print("underflow")


queue = Queue()

flag = 0
while flag == 0:
    ch = int(input("enter 1 to push\nenter 2 to pop\nenter 3 to display\nenter your choice: "))
    if (ch == 1):
        queue.push()
    elif (ch == 2):
        queue.pop()
    elif (ch == 3):
        queue.display()
    else:
        print("Invalid Choice")

    flag = int(input("enter 1 to exit\nenter 0 to continue\nenter your choice: "))



