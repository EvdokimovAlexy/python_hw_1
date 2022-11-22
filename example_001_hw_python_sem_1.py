num = int(input('Введите день недели\n'))
if 5 < num < 8:
    print('Этот день выходной')
elif 7 < num or num < 0:
    print('В недели только 7 дней, ошибка ввода')
else:
    print('Рабочий день')