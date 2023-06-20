def temperatureConverter(temp):
    f = int(temp * 1.8 + 32)
    k = int(temp - 273.15)
    
    return (f'{f}F e {k}K')


print(temperatureConverter(15))