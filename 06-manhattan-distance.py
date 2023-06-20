def manhattanDistance(x1, y1, x2, y2): 
    x = (x1 - x2)
    y = (y1 - y2)
    
    if x < 0 :
      x *= -1
    
    if y < 0 :
      y*= -1
    
    return x + y

print(manhattanDistance(2.5, -0.4, -12.2, 7.0))