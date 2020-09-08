class Multiset:
    mset=[]
    def add(self, val):
        self.mset.append(val)
    

    def remove(self, val):
        if(val in self.mset):
            n=len(self.mset)
            i=0
            while i<n:
                if self.mset[i]==val:
                    self.mset=self.mset[0:i]+self.mset[i+1:]
                    n=n-1
                else:
                    i=i+1
        

    def contains(self, val):
        print("co")
        if(val in self.mset):
            print("t")
            return True
        else:
            print("f")
            return False
    
    def len(self):
        return len(self.mset)
    
    def disp(self):
        print(self.mset)

if __name__ == '__main__':
    m=Multiset()
    m.add(5)
    m.add(6)
    m.add(5)
    m.add(3)
    m.contains(4)
    m.contains(5)
    m.disp()
    m.remove(5)
    m.disp()