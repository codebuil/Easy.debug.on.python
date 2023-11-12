buglist=[50,51,53,54,55,56]
stages=0
def stagesf()->int:
    global stages
    stages+=1
    if stages==100:
        stages=0
    return stages

def log(func,vars:str,into:int)->int:
    bugstop=False
    r=not(into)
    
    while r!=into:
        r=func()
        for nn in buglist:
            if r==nn:
                bugstop=True
        f1=open ("log.txt","a")
        f1.write(f"{r}=func"+vars+" \n")
        if bugstop:
            f1.write("error on number:"+str(r)+"\n")
        f1.close()
        if bugstop:
            print("error on number:"+str(r))
            raise Exception 
    return r
  
def logclear():
        f1=open ("log.txt","w")
        f1.write("")
        f1.close()

print("\x1bc\x1b[43;30m")

logclear()
r=log(stagesf,".....",0)