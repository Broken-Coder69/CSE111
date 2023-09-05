class Test4:
    def __init__(self):
        self.sum, self.y = 0, 0
    def methodA(self):
        x, y = 0, 0
        msg = [0]
        msg[0] = 5
        y = y + self.methodB(msg[0])
        x = y + self.methodB(msg, msg[0])
        self.sum = x + y + msg[0]
        print(x, y, self.sum)
    def methodB(self, *args):
        if len(args) == 1:
            mg1 = args[0]
            x, y = 0, 0
            y = y + mg1
            x = x + 33 + mg1
            self.sum = self.sum + x + y
            self.y = mg1 + x + 2
            print(x, y, self.sum)
            return y
        else:
            mg2, mg1 = args
            x = 0
            self.y = self.y + mg2[0]
            x = x + 33 + mg1
            self.sum = self.sum + x + self.y
            mg2[0] = self.y + mg1
            mg1 = mg1 + x + 2
            print(x, self.y, self.sum)
            return self.sum

t3 = Test4()
t3.methodA()
t3.methodA()
t3.methodA()
t3.methodA()
