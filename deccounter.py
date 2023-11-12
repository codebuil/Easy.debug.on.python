import random
counts=5
scounts=5
def dcounters()->int:
    global counts
    global scounts
    counts-=1
    if counts==-1:
        counts=scounts
    return counts
    
    
def  debugs(func)->int:
    r=func()
    print(f"{r}=func")
    return r
  

a=0
for n in range(0,10):
    a=debugs(dcounters)