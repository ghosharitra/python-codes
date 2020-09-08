class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def display(self):
        print("Stack: ", end="")
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
            p = self.head
            if p.next==None:
                x = p.data
                self.head=None
                print("popped element: ", x)
            else:
                while p.next.next!=None:
                    p=p.next
                x = p.next.data
                p.next=None
                print("popped element: ", x)
        else:
            print("underflow")


stack = Stack()

flag = 0
while flag == 0:
    ch = int(input("enter 1 to push\nenter 2 to pop\nenter 3 to display\nenter your choice: "))
    if ch == 1:
        stack.push()
    elif ch == 2:
        stack.pop()
    elif ch == 3:
        stack.display()
    else:
        print("Invalid Choice")

    flag = int(input("enter 1 to exit\nenter 0 to continue\nenter your choice: "))



