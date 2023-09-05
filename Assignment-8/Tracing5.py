class A:
  temp = 3
  def __init__(self):
    self.sum = 0
    self.y = 0
    self.y = A.temp - 1
    self.sum = A.temp + 2
    A.temp -= 2
  
  def methodA(self, m, n):
    x = 0
    n[0] += 1
    self.y = self.y + m + A.temp
    A.temp += 1
    x = x + 2 + n[0]
    n[0] = self.sum + 2
    print(f"{x} {self.y} {self.sum}")
 
class B(A):
  x = 1
  def __init__(self, b = None):
    super().__init__()
    self.sum = 2
    if b == None:  
      self.y = self.temp + 1    
      B.x = 3 + A.temp + self.x
      A.temp -= 2
    else:
      self.sum = self.sum + self.sum
      B.x = b.x + self.x
  def methodB(self, m, n):
    y = [0]
    self.y = y[0] + self.y + m
    B.x = self.y + 2 +  self.temp - n
    self.methodA(self.x, y)
    self.sum = self.x + y[0] + self.sum
    print(f"{self.x} {y[0]} {self.sum}")

x = [23]
a1 = A()
b1 = B()
b2 = B(b1)
a1.methodA(1, x)
b2.methodB(3, 2)
a1.methodA(1, x)




