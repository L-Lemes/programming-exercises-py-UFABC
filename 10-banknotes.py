def banknotes(value):
    hundred = int(value / 100)
    fifty = int((value - (hundred * 100)) / 50)
    twenty = int((value - (hundred * 100) - (fifty * 50)) /20)
    ten = int((value - (hundred * 100) - (fifty * 50) - (twenty * 20)) /10)
    five = int((value - (hundred * 100) - (fifty * 50) - (twenty * 20) - (ten * 10)) /5)
    two = int((value - (hundred * 100) - (fifty * 50) - (twenty * 20) - (ten * 10) - (five * 5)) /2)
    one = int((value - (hundred * 100) - (fifty * 50) - (twenty * 20) - (ten * 10) - (five * 5) - (two * 2)) /1)

    return (f'{hundred} de 100, {fifty} de 50, {twenty} de 20, {ten} de 10, {five} de 5, {two} de 2 e {one} de 1')

print(banknotes(642))

    
