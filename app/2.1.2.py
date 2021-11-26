mas, rost = float(input()), float(input())
if mas/(rost**2) > 25:
    print('Избыточная масса')
elif mas/(rost**2) < 18.5:
    print('Недостаточная масса')
else:
    print('Оптимальная масса')