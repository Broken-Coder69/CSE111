class msgClass:
    def __init__(self):
        self.content = 0
class Q5:
    def __init__(self):
        self.sum = 1
        self.x = 2
        self.y = 3 
    def methodA(self):
        x, y = 1, 1
        msg = []
        myMsg = msgClass()
        myMsg.content = self.x
        msg.append(myMsg)
        msg[0].content = self.y + myMsg.content
        self.y = self.y + self.methodB(msg[0])
        y = self.methodB(msg[0]) + self.y
        x = y + self.methodB(msg[0], msg)
        self.sum = x + y + msg[0].content
        print(x," ", y," ", self.sum)
    def methodB(self, mg1, mg2 = None):
        if mg2 == None:
            x, y = 5, 6
            y = self.sum + mg1.content
            self.y = y + mg1.content
            x = self.x + 7 +mg1.content
            self.sum = self.sum + x + y
            self.x = mg1.content + x +8
            print(x, " ", y," ", self.sum)
            return y
        else:
            x = 1
            self.y += mg2[0].content
            mg2[0].content = self.y + mg1.content
            x = x + 4 + mg1.content
            self.sum += x + self.y
            mg1.content = self.sum - mg2[0].content
            print(self.x, " ",self.y," ", self.sum)
            return self.sum

q = Q5()
q.methodA()