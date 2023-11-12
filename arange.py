def arange(a:int)->int:
  b=[9,8,7,6,5,4,3,2,1,0,-1]
  
  if a>=len(b) or a<0:
    return -1
  
  return b[a]

def debug(func,a):
  r=func(a)
  print(f"{r}=func,{a}")

print("\x1bc\x1b[43;30m")

for n in range(-20,20,1):
    r=debug(arange,n)
