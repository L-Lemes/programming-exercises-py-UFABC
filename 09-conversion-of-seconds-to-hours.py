def conversionOfSecondsToHours(x):
  if x >= 0: 
    hourInt = int(x / 3600)
    minInt = int((x / 60) - 60)
    secInt = int( x - (hourInt * 3600) - (minInt * 60))

    hour = hourInt
    min = minInt
    sec = secInt

    if hourInt < 10:
      hour = str(hourInt)
      hour = '0' + hour

    if minInt < 10:
      min = str(minInt)
      min = '0' + min

    if secInt < 10:
      sec = str(secInt)
      sec = '0' + sec

    return (f'{hour}:{min}:{sec}')

  return (f'Número de segundos invalido, informe um valor maior que zero')

print(conversionOfSecondsToHours(3600))