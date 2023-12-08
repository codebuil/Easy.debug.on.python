
class jumps:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items=  [item]  + self.items 

    def pop(self, item ):
        for n in range(len(self.items)-1):
            if self.items[n] == item:
                self.items.pop(n)
        return None

    def report(self):
        print(self.items)


print("\x1bc\x1b[43;30m")
jumps1=jumps()
jumps1.push("a")
jumps1.push("b")
jumps1.push("c")
jumps1.report()
a=jumps1.pop('b')
jumps1.report()
