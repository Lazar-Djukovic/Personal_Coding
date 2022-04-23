import math

class Point:
  def __init__(self, x:float, y:float) -> None:
      self.move(x,y)

  def move(self, x:float, y:float):
    self.x = x
    self.y = y
  
  def reset(self):
    self.x = 0
    self.y = 0

  def calculate_distance(self, p):
    return math.hypot(self.x - p.x, self.y - p.y)

  
p1 = Point(3,5)
p2 = Point(0, 1)
#p1.reset()
p2.move(5,0)
print(p2.calculate_distance(p1))

assert p2.calculate_distance(p1) == p2.calculate_distance(p1)

p1.move(3,4)
print(p1.calculate_distance(p2))

print(p1.calculate_distance(p1))

