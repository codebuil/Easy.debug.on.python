buglist=[50,51,53,54,55,56]

def prod(a:int)->int:
    
    return a*a

def buginject(func,vars:str,into:int)->int:
    bugstop=False
    r=0
    f2=open ("list.txt","w")
        
        
    for r in range(0,into):
        rr=func(r)
        f2.write(f"{rr}\n")
        for nn in buglist:
            
            if rr==nn:
                bugstop=True
        f1=open ("log.txt","a")
        f1.write(f"{rr}=func,{r},"+vars+" \n")
        if bugstop:
            f1.write("error on number:"+str(rr)+"\n")
        f1.close()
        if bugstop:
            print("error on number:"+str(rr))
            f2.close()
            raise Exception 
    f2.close()
    return r
  
def logclear():
        f1=open ("log.txt","w")
        f1.write("")
        f1.close()

print("\x1bc\x1b[43;30m")

logclear()
r=buginject(prod,".....",100)