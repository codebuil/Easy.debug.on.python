def bools(a:int)->int:
  if a!=0:
    return 1
  return 0

def debug(func,a):
  r=func(a)
  print(f"{r}=func,{a}")

print("\x1bc\x1b[43;30m")

for n in range(-20,20,1):
    r=debug(bools,n)
