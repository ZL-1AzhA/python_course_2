t, r = input(), input()
if (t == 'камень' and r == 'ножницы') or (t == 'бумага' and r == 'камень') or (t == 'ножницы' and r == 'бумага'):
    print('Тимур')
elif r == t:
    print('ничья')
else:
    print('Руслан')