
class stacks:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items=  [item]  + self.items 

    def pop(self):
        return self.items.pop(0)

    def report(self):
        print(self.items)


print("\x1bc\x1b[43;30m")
stacks1=stacks()
stacks1.push("a")
stacks1.push("b")
stacks1.push("c")
stacks1.report()
a=stacks1.pop()
stacks1.report()
a=stacks1.pop()
stacks1.report()