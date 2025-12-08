# Дао Ань Туан, ИУ7И-14Б, Цель программы: Посчитать биссектрису, проведенной к наименьшей стороне и определить лежит ли заданная точка внутри треугольника
# Ввод данных
alphabet = 'qwertyuiopasdfghjklzxcvbnm '
x = input('Введите 3 координата x по пробелу: ').split()

#Проверка условий
error = False
if len(x) != 3:
    print('Ошибка было введено более/менее 3 координат')
    error = True
#Проверка на буквы и пустую строку
elif len(x) == 3:
    for num in x:
        for l in alphabet:    
            if l in num:
                print('Некорректные данные, было введены буквы/пустая строка. Введите числа')
                error = True
                break
        if error:
            break
#Проверка на максимальную координату
    if not error:
        if float(x[0]) > 1e10 or float(x[1]) > 1e10 or float(x[2]) > 1e10:
            print('Слишком большое значение координаты. Оно не должно превышать 1e10')
            error = True
#Если в x не были найдены ошибки, проверяется анологично y
if not error:
    y = input('Введите 3 координата y по пробелу: ').split()
    if len(y) != 3:
        print('Ошибка было введено более/менее 3 координат')
        error = True

    elif len(y) == 3:
        for num in y:
            for l in alphabet:    
                if l in num:
                    print('Некорректные данные, было введены буквы/пустая строка. Введите числа')
                    error = True
                    break
            if error:
                break

        if not error:
            if float(y[0]) > 1e10 or float(y[1]) > 1e10 or float(y[2]) > 1e10:
                print('Слишком большое значение координаты. Оно не должно превышать 1e10')
                error = True

#Если ошибок не возникло вообще
if not error:
    print('Success')
    x = list(map(float, x))
    y = list(map(float, y))
    #Уравнение прямой по 2 точкам
    if (x[2] - x[0]) * (y[1] - y[0]) == (y[2] - y[0]) * (x[1] - x[0]):
        print('Ошибка, введенные координаты не образуют треугольник')
        error = True

    if not error:
        #Точки
        dot_A = [x[0], y[0]]
        dot_B = [x[1], y[1]]
        dot_C = [x[2], y[2]]
    
        #Определение длин сторон через длину вектора
        AB = ((dot_B[0]-dot_A[0])**2 + (dot_B[1]-dot_A[1])**2)**0.5
        CA = ((dot_A[0]-dot_C[0])**2 + (dot_A[1]-dot_C[1])**2)**0.5
        BC = ((dot_C[0]-dot_B[0])**2 + (dot_C[1]-dot_B[1])**2)**0.5

        #Находим квадраты сторон
        ab2 = AB**2
        bc2 = BC**2
        ca2 = CA**2
        if AB == CA or AB==BC or CA==BC:
            print('Треугольник равнобедренный')
        #Проверяем теорему Пифагора
        if ab2 - (bc2 + ca2)==0:
            print('Треугольник прямоугольный (прямой угол в вершине C)')
            if BC <= CA:
                numerator = AB * CA * ((AB + CA)**2 - BC**2)
                l = (numerator ** 0.5) / (AB + CA)
                print(f'Биссектриса к наименьшей стороне BC: {l:.6f}')
            else:
                numerator = AB * BC * ((AB + BC)**2 - CA**2)
                l = (numerator ** 0.5) / (AB + BC)
                print(f'Биссектриса к наименьшей стороне CA: {l:.6f}')

        elif bc2 - (ab2 + ca2)==0:
            print('Треугольник прямоугольный (прямой угол в вершине A)')
            if AB <= CA:
                numerator = CA * BC * ((CA + BC)**2 - AB**2)
                l = (numerator ** 0.5) / (CA + BC)
                print(f'Биссектриса к наименьшей стороне AB: {l:.6f}')
            else:
                numerator = AB * BC * ((AB + BC)**2 - CA**2)
                l = (numerator ** 0.5) / (AB + BC)
                print(f'Биссектриса к наименьшей стороне CA: {l:.6f}')

        elif ca2 - (ab2 + bc2)==0:
            print('Треугольник прямоугольный (прямой угол в вершине B)')
            if AB <= BC:
                numerator = CA * BC * ((CA + BC)**2 - AB**2)
                l = (numerator ** 0.5) / (CA + BC)
                print(f'Биссектриса к наименьшей стороне AB: {l:.6f}')
            else:
                numerator = AB * CA * ((AB + CA)**2 - BC**2)
                l = (numerator ** 0.5) / (AB + CA)
                print(f'Биссектриса к наименьшей стороне BC: {l:.6f}')
        #Срабатывает если треугольник не прямоугольный
        else:
            #Находим минимальную сторону и вычисляем биссектрису
            if AB <= CA and AB <= BC:
                numerator = CA * BC * ((CA + BC)**2 - AB**2)
                l = (numerator ** 0.5) / (CA + BC)
                print(f'Биссектриса к наименьшей стороне AB: {l:.6f}')

            elif CA <= AB and CA <= BC:
                numerator = AB * BC * ((AB + BC)**2 - CA**2)
                l = (numerator ** 0.5) / (AB + BC)
                print(f'Биссектриса к наименьшей стороне CA: {l:.6f}')

            else:
                numerator = AB * CA * ((AB + CA)**2 - BC**2)
                l = (numerator ** 0.5) / (AB + CA)
                print(f'Биссектриса к наименьшей стороне BC: {l:.6f}')
            
            #Пользовательский ввод
            user_input = list(map(float, input('Введите координату x и y: ').split()))
            px, py = user_input[0], user_input[1]
            # Площадь треугольника ABC
            area_abc = abs((dot_B[0]-dot_A[0])*(dot_C[1]-dot_A[1]) - (dot_C[0]-dot_A[0])*(dot_B[1]-dot_A[1])) / 2
            # Площадь ABP
            area_abp = abs((dot_B[0]-dot_A[0])*(py-dot_A[1]) - (px-dot_A[0])*(dot_B[1]-dot_A[1])) / 2
            # Площадь BCP  
            area_bcp = abs((dot_C[0]-dot_B[0])*(py-dot_B[1]) - (px-dot_B[0])*(dot_C[1]-dot_B[1])) / 2
            # Площадь CAP
            area_cap = abs((dot_A[0]-dot_C[0])*(py-dot_C[1]) - (px-dot_C[0])*(dot_A[1]-dot_C[1])) / 2
            # Проверка
            if area_abp + area_bcp + area_cap == area_abc:
                print('Точка внутри треугольника')
            else:
                print('Точка снаружи треугольника')