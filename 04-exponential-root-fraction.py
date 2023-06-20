def exponentialRootFraction(a,b,x,y):
    expression = round((float(a + b**x - b**(1/2) + ((a + b) / ( x - y)))), 2)
    
    return (f'expressão: {expression}')
  

print(exponentialRootFraction(1, 2, 1.1, 2.2))