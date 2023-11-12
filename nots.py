import random

def nots(a:int):
    if a==0:
        return 1
    return 0
    
    
def  debugs(func,a:int)->int:
    r=func(a)
    print(f"{r}=func,{a}")
    return r
  

a=0
print(a)
for n in range(0,10):
    a=debugs(nots,a)