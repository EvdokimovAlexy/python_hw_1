x = int(input('Введите координату x: \n'))
y = int(input('Введите координату y: \n'))
if x > 0 and y > 0:
    print('Плоскость № 1')
elif (x < 0) and y > 0:
    print('Плоскость № 2')
elif x < 0 and y < 0:
    print('Плоскость № 3')
elif (x > 0) and y < 0:
    print('Плоскость №4')