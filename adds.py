def adds(a:int,b:int)->int:
  return a+b

def debug2(func,a,b):
  r=func(a,b)
  print(f"{r}=func,{a},{b}")

print("\x1bc\x1b[43;30m")

for n in range(-20,20,1):
    r=debug2(adds,n,n+20)

