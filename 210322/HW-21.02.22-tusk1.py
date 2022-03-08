while True:
    x = int(input('Введите значеине:\n'))
    sec = (x % 60)
    mins = (x // 60 % 60)
    hours = (x // 3600 % 24)
    days = (x // 86400 % 30)
    print(x)
    print(f'{days} Дней', f'{hours} Часов', f'{mins} минут', f'{sec} секунд')


