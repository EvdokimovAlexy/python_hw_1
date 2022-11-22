from math import sqrt
xa = int(input('Введите координату xa: \n'))
ya = int(input('Введите координату ya: \n'))
xb = int(input('Введите координату xb: \n'))
yb = int(input('Введите координату yb: \n'))
dist = round(sqrt((xb-xa)**2 + (yb-ya)**2), 2)
print(dist)