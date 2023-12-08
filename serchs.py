import random
class finders:
    def __init__(self):
        self.items = []

    def apps(self):
        self.push(random.randint(1,50))

  
    def push(self, item):
        self.items=  [item]  + self.items 

    def getn(self):
        return self.items[random.randint(0,len(self.items)-1)]
    def pop(self, item ):
        nn=0
        nn=len(self.items)
        maxn=nn
        minn=0
      
        if nn==0:
          return None
        nn=nn//2
        bin=0
        outs=True
        while outs:
          print("__"+str(nn))
          if self.items[nn] == item:
              tt=self.items.pop(nn)
              return tt
          elif self.items[nn] > item:
            maxn=nn-1
            nn=(maxn-minn)//2+minn
 
          elif self.items[nn] < item:
              minn=nn+1
              nn=(maxn-minn)//2+minn
        
          if minn==maxn:
            outs=False
          if self.items[nn] == item:
              tt=self.items.pop(nn)
              return tt
        return None

    def report(self): 
        self.items.sort()
        print(self.items)

 
print("\x1bc\x1b[43;30m")
fnd=finders()
for n in range(12): 
  fnd.apps()  
fnd.report()
tt=fnd.getn()
print(tt)
tt=fnd.pop(tt)
fnd.report()
print(tt)
