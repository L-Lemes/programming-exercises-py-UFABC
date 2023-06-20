def salary(name, fixedSalary, sales, percentageOnSales):
    
    finalSalary = round(float(fixedSalary + (sales * percentageOnSales / 100)), 2)
    
    return (f'{name} dev receber R$ {finalSalary}')

print(salary('Maria', 2100.78, 10000, 7))