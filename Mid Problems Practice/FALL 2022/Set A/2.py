class MidA:
    def __init__(self):
        self.x = 4
        self.y = 1
        self.sum = 3
        
        
    def methodA(self, x):
        self.y = self.sum + self.x + x
        self.sum = x + self.y
        d = MidA()
        d.sum = self.sum + self.methodB(d)
        print(self.x, self.y, self.sum)
        
        
    def methodB(self, t, z=0):
        y = 3
        t.x = self.x + self.sum
        self.sum = t.x + t.y + y
        print(t.x, t.y, t.sum)
        if z == 0:
            return t.sum


a = MidA()
a.methodA(4)
a.methodB(a, 99)