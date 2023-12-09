
import random
class items:
 def __init__(self,value):
   self.value=value
   self.next=None
   

class lists:
  def __init__(self):
      self.count=0
      self.root=None
      self.last=None

  def add(self,value):
    if self.root==None:
      a=items(value)
      self.root=a
      self.last=a
    else:
      a=items(value)
      self.last.next=a
      self.last=a
      
    self.count+=1

  def prints(self):
    a=self.root
    print ("[ ",end="")
    for n in range(self.count):
      print(a.value,end="")
      if n<self.count-1:
          print (" , ",end="")
      a=a.next
    print (" ]")

print("\x1bc\x1b[43;30m")
l1=lists()
for n in range(12):
  l1.add(random.randint(0,50))
l1.prints()
