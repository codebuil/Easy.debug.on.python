
class texts:
    def __ini__(self,value):
      self.lines=""
      self.lines=value.split("\n")

    def toTexts(self,value):
      self.lines=value.split("\n")

    def toStrings(self):
      return "\n".join(self.lines)
      
vs="""arm
    arm7
    arm8
x86 
    8086
    80286
    80386
    80486"""



print("\x1bc\x1b[43;30m")
txts=texts()
txts.toTexts(vs)
txts.lines.append("    80586")
print(txts.toStrings())
