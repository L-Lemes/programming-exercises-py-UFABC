def installments(value, installmentsNumber):
    installments = round(float(value / installmentsNumber), 2)

    return (f'R$: {installments}')

print(installments(7985.64, 24))