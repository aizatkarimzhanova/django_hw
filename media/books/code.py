

#В ДЗ №1 код просил Вас ввести расход дня 7 раз,
#  по сути там было повторение одного и того же
#  - поэтому постарайтесь переделать его
#  с использованием циклов for или while и
#  списков либо кортежей на выбор.
#  Код должен стать короче, количество строк должно уменьшиться.


#wednesday  = int(input('рассходы в ср: '))
#thursday = int(input('рассходы в чт: '))
#friday = int(input('рассходы в пт: '))
#satirday = int(input('рассходы в сб: '))
#sunday = int(input('рассходы в вс: '))
#summ = monday + tuesday + wednesday + thursday + friday + satirday + sunday
#sr_summ = int(summ // 7)
#print(summ)
#print(sr_summ)

summ_day = 0
counter = 1
while counter < 8:
    day = int(input(f'рассходы на день {counter}: '))
    counter += 1
    summ_day += day

sr_summ = int(summ_day // 7)
print(summ_day)
print(sr_summ)


while True:
    color = input('ввести цвет светофора(зеленый, желтый, красный): ').lower()
    if color == 'выход':
        break
    if color == 'зеленый':
        print('можно')
    elif color == 'желтый':
        print('готовься')
    elif color == 'красный':
        print('стоп')
    else: 
        print('всё, кроме "зеленый", "желтый", "красный", "выход" считается неверным запросом')



