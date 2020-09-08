class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def print(self):

        p = self.head
        while p.next != None:
            print(p.data, "->", end="")
            p = p.next
        print(p.data)

    def insert(self):
        new = Node(input())

        if (self.head == None):
            self.head = new
        else:
            p = self.head
            while p.next != None:
                p = p.next
            p.next = new


ll = LinkList()
# ll.head=Node("a")
# b=Node("b")
# c=Node("c")

# ll.head.next=b
# b.next=c

# ll.print()
for i in range(int(input("enter no. of nodes: "))):
    ll.insert()

ll.print()
