import random
counts=0
scounts=5
def scounters()->int:
    global counts
    global scounts
    counts+=1
    if counts==scounts:
        counts=0
    return counts
    
    
def  debugs(func)->int:
    r=func()
    print(f"{r}=func")
    return r
  

a=0
for n in range(0,10):
    a=debugs(scounters)