def secondDegreeEquation(a, b, c, x):
    if a != 0:
      xOne = round(float((-b + (b ** 2 - 4 * a * c))/2 * a), 2)
      xTwo = round(float((-b - (b ** 2 - 4 * a * c))/2 * a), 2)
      result = round(float(a* (x**2) + b * x + c), 2)

      return {
        'x1': xOne,
        'x2': xTwo,
        'result': result
      }
    return (f'O valor de a invalido, escreva um numero diferente de 0')

print(secondDegreeEquation(0, -5, 6, 2))

