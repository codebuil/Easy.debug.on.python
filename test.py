import random
def incr(counts)->int:
    return counts+1
    
    
def  tests(func,starts:int,ends:int)->int:
    for nn in range(starts,ends):
        r=func(nn)
        print(f"{r}=func,{nn}")
    return r
  

a=tests(incr,0,10)