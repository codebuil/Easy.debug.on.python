import random
class llist:
    def __init__(self):
        self.lists=[]
        for n in range(12):
            self.lists.append(random.randint(1,50))
    @property
    def gets(self)->list:
       return self.lists

class listlistss:
  def __init__(self):
      self.lists=[]
      for n in range(3):
         
          self.lists.append(llist())

  
  def report(self):
      for n in self.lists:
          
          print(n.gets)


class listlists:
    def __init__(self):
        self.lists=[]
        
        for n in range(3):
            self.lists.append(listlistss())
    

    def report(self):
      for n in self.lists:
        print("------------------------------")
        n.report()
 
print("\x1bc\x1b[43;30m")
l1=listlists()
l1.report()

