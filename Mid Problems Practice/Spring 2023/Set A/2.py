#TRACING

class MidA:
    def __init__(self):
        self.y = 2
        self.z = 3
        self.sum =-1
        
        
    def m1(self, mg2, mg1=2):
        x = 0
        self.y = self.y + mg2[0]
        x += 33 + mg1
        self.sum += x + self.y
        mg2[0] = self.y + mg1
        mg1 = mg1 + x + 2
        print(x, self.y, self.sum)
        
        
    def m2(self, y=3):
        mid = [0]
        mid[0] = 7
        self.m1(mid, mid[0])
        z = y + mid[0]
        y = self.y + mid[0]
        self.sum = z + y + mid[0]
        print(z, y, self.sum)
        
        
a = MidA()
a.m1([6])
a.m2()