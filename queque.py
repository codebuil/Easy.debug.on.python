class queque:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items=   self.items + [item]

    def pop(self):
        return self.items.pop(0)

    def report(self):
        print(self.items)


print("\x1bc\x1b[43;30m")
queque1=queque()
queque1.push("a")
queque1.push("b")
queque1.push("c")
queque1.report()
a=queque1.pop()
queque1.report()
a=queque1.pop()
queque1.report()
