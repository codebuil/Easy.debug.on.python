import random
counts=0
def counters()->int:
    global counts
    counts+=1
    return counts
    
    
def  debugs(func)->int:
    r=func()
    print(f"{r}=func")
    return r
  

a=0
for n in range(0,10):
    a=debugs(counters)