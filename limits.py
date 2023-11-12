def alimits(a:int,b:int,c:int)->int:
  if a <= b:
    return b
  if a >= c:
    return c
  
  return a

  return b[a]

def debug3(func,a,b,c):
  r=func(a,b,c)
  print(f"{r}=func,{a},{b},{c}")

print("\x1bc\x1b[43;30m")

for n in range(-20,20,1):
    r=debug3(alimits,n,0,11)