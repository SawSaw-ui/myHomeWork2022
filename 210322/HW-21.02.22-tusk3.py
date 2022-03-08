while True:
    rate = int(input('Введите кол-во процентов:\n'))
    if (rate % 10 == 1) and (rate != 11) and (rate != 111):
        print(f'{prcent} процент!')
    elif (rate % 10 > 1) and (rate % 10 < 5) and (rate != 12, 13, 14):
        print(f'{rate} процента!')
    elif (rate == 0):
        print('нулевое значение!')
        break
    else:
        print(f'{rate} процентов!')
