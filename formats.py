class fileformat:
    def __init__(self,files):
        self.contents=""
        f1=open(files,"r")
        self.contents=f1.read()
        f1.close()

    def report(self,i):
        ss=self.contents.split("\n")
        for n in ss:
            count=0
            tt=True
            n=n+"\n"
            while tt:
                nn=count+i
                if nn>len(n):
                    nn=len(n)
                    tt=False
                n=n.replace("\r","")
                print(n[count:nn],end="")
                count+=i
                if count>len(n):
                    tt=False 
                 
                
      
print("\x1bc\x1b[43;30m")
f1=fileformat("my.txt")
f1.report(20)
