


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None
        self.count=0

    def display(self):
      print("Linked list: ",end="")
      if self.head==None:
        print("Empty")
      else:
        p = self.head
        while p.next != None:
            print(p.data, " -> ", end="")
            p = p.next
        print(p.data)

    def finsert(self,data):
        self.count+=1
        new = Node(data)

        if self.head == None:
            self.head = new
        else:
            new.next=self.head
            self.head=new

            
    def linsert(self,data):
        self.count+=1
        new = Node(data)

        if self.head == None:
            self.head = new
        else:
            p=self.head
            while p.next!=None:
              p=p.next
            p.next=new

    def minsert(self,data):
      new = Node(data)
      pos=int(input("enter position: "))
      if self.head == None:
          self.head = new
          self.count+=1
      else:
          p=self.head
          if 0<pos and pos<=self.count+1:
            if pos==1:
              self.finsert(data)
            elif pos==self.count+1:
              self.linsert(data)
            else:
              self.count+=1
              i=0
              while i<pos-2:
                p=p.next
              q=p.next
              p.next=new
              new.next=q
          else:
            print("invalid position")
                
                



   


ll = LinkList()
# ll.head=Node("a")
# b=Node("b")
# c=Node("c")

# ll.head.next=b
# b.next=c

# ll.print()
for i in range(int(input("enter no. of nodes: "))):
    #ll.finsert()
    #ll.linsert()
    
    ll.minsert(input("enter data:"))

ll.display()
ert(input("enter data:"))

ll.display()
