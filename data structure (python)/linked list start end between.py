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

        p=self.head
        if 0<pos and pos<=(self.count+1):
            if pos==1:
                self.count+=1
                new.next=self.head
                self.head=new
            
            else:
                p=self.head
                self.count+=1
                i=0
                #print("else entered: " ,end="")
                while i<(pos-2):
                    #print(p.data, end="")
                    p=p.next
                    i+=1
                q=p.next
                p.next=new
                new.next=q
        else:
            print("invalid position")

            
    def fremove(self):
        if self.head==None:
            print("underflow")
        else:
            self.count -= 1
            x=self.head.data
            self.head=self.head.next
            print("removed data: ",x )

            
    def lremove(self):
        if self.head==None:
            print("underflow")
        else:
            self.count -= 1
            p=self.head
            if p.next==None:
                x=p.data
                self.head=None
                print("removed data: ",x )
            else:
                while p.next.next!=None:
                    p=p.next
                x=p.next.data
                p.next=None
                print("removed data: ",x )
    
    
    def mremove(self):
        pos=int(input("enter position: "))
        if self.head==None:
            print("underflow")
        else:
            self.count -= 1
            if 0<pos and pos<=(self.count):
                if pos==1:
                    x=self.head.data
                    self.head=self.head.next
                    print("removed data: ",x )
                else:
                    p=self.head
                    i=0
                    while i<pos-2:
                        p=p.next
                        i+=1
                    x=p.next.data
                    p.next=p.next.next
                    print("removed data: ",x )
            
            
            
            
            
            
            else:
                print("invalid position")
                
                
                
                

ll = LinkList()
flag=0
print("enter 1 to insert at first\nenter 2 to insert in between\nenter 3 to insert at last\nenter 4 to delete from first\nenter 5 to delete from in between\nenter 6 to delete from last\nenter 7 to display\n")
while flag!=1:
    ch=int(input("enter your choice: "))    
    if(ch==1):
       ll.finsert(input("enter data:"))
    elif(ch==2):
        ll.minsert(input("enter data:"))
    elif(ch==3):
        ll.linsert(input("enter data:"))
    elif(ch==4):
        ll.fremove()
    elif(ch==5):
        ll.mremove()
    elif(ch==6):
        ll.lremove()
    elif(ch==7):
        ll.display()
    else :
        print("Invalid Choice")
        
    flag=int(input("enter 1 to exit\nenter 0 to continue\nenter your choice: ")) 
 

ll.display()
