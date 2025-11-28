#Дао Ань Туан, ИУ7И-14Б, Задача: посчитать значение y при введенных пользователем коэфицент 

#Ввод данных
coefficient_a = float( input('Введите коэфицент a чтобы задать квадратное уравнение: ') )
coefficient_b = float( input('Введите коэфицент b чтобы задать квадратное уравнение: ') )
coefficient_c = float( input('Введите коэфицент c чтобы задать квадратное уравнение: ') )

#Решение уравнения и вывод ответов
if coefficient_a == 0:

    if coefficient_b == 0:
        print('Нет решений, график константы')

    elif coefficient_b == 0 and coefficient_c == 0:
        print('Бесконечное кол-во решений')

    else:
        x = -coefficient_c / coefficient_b
        print(f'Корень уравнения: {x:g}')

else:
    
    D = (coefficient_b**2 - 4 * coefficient_a * coefficient_c)
    if D == 0:
        x = -coefficient_b / 2*coefficient_a
        print(f'Корень уравнения: {x:g}')

    elif D < 0:
        print('Нет корней, дискриминант отрицательный')

    else:
        x1 = (-coefficient_b + D**0.5) / (2*coefficient_a)
        x2 = (-coefficient_b - D)**0.5 / 2*coefficient_a
        print(f'Корни уравнения: {x1:.6g}, {x2:6g}')

#Часть 2
#Задание 1
#ввод данных
'''x = float( input('Введи значение х: ') )
y = None

if x >= 8:
    y = (x - 4) / 2

elif x <= -6:
    y = -(x - 4) / 2 - 10

elif -6 <= x < 4:
    y = -(x / 2)**2 + 4

elif -4 <= x < 8:
    y = (x - 4)**0.5

else:
    print('Введенное значение х не соответсвует условию ')

print(y)'''

#Задание 2
'''alphabet = 'qwertyuiopasdfghjklzxcvbnm'

# Ввод данных
x_input = input('Введите х: ')
y_input = input('Введите y: ')

# Проверка на пустую строку
if x_input == '' or y_input == '':
    print('Вы ввели пустую строку')
else:
    # Проверка на наличие букв в строке
    letter_inside_x = False
    letter_inside_y = False
    for char in x_input:
        if char.lower() in alphabet:
            letter_inside_x = True
            break
    for char in y_input:
        if char.lower() in alphabet:
            letter_inside_y = True
            break
    
    if letter_inside_x or letter_inside_y:
        print('Введенные данные не являются числом')
    else:
        x = float(x_input)
        y = float(y_input)
        
        # Проверка на бесконечность
        if x < 1e10 and y < 1e10:
            if ((y >= -3 * x / 4 - 4) and (y <= x / 4 - 0.5) and (y >= 2 * x - 4)) or \
               ((y >= x / 4 - 0.5) and (y <= 2 * x - 4) and (y <= -(x - 4)**2 + 4)):
                print('Точка входит в область')
            else:
                print('Точка не входит в область')
        else:
            print('Точка не лежит в области')

'''
#4<=x<5.75




