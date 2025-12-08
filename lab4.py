#Дао Ань Туан ИУ7И-14Б, Цель программы: вычислить сумму последовательности чисел до точности эпсилон

#Пользовательский ввод
n_max = int(input('Выбери n: '))
max_iteration = int(input('Максимальное кол-во итераций: '))
ε = float(input('Введи точность эпсилон: '))
steps = int((input('Введите шаг печати: ')))

k = 1
s = 1
precision_achieved = False
error = False

'''if not n_max.isdigit() or not  max_iteration.isdigit() or not steps.isdigit():
    error = True
    print('Ошибка: n, максимальное количество итераций и шаг печати должны быть целыми числами')
else:
    n_max = int(n_max)
    max_iteration = int(max_iteration)
    steps = int(steps)

if '.' in ε and ε.count('.') == 1:
    l = ε.split('.')
    if l[0].isdigit() and l[1].isdigit():
        ε = float(ε)
    else:
        error = True
else:
    error = True'''

if not error:
    #Создание таблицы 
    print("-" * 48)
    print(f"|{'Итерация':^10} | {'Текущий член':^15} | {'Сумма':^15}|")
    print("-" * 48)

    #Логика функции(прохождение от 1 до максимального n)
    for n in range(2, n_max + 1):
        numerator = -1
        numbers = map(int, ('-1 ' * (n - 2) ).split())
        for neg_one in numbers:
            numerator *= neg_one

        current_number = numerator / (2 * n - 1)
        s += current_number
        k += 1
        if n == 2:
            print(f'|{1:^10} | {1:^15.8f} | {1:^15.8f}|')
        #Печатаем на каждом шаге печати и 1 итерации
        if k % steps == 0 or k == 1:
            print(f'|{k:^10} | {current_number:^15.8f} | {s:^15.8f}|')
        
        #Проверяем точность
        if abs(current_number) < ε:
            print("-" * 48)
            print(f'Текущий член по модулю ({current_number:.8f}) < ε ({ε})')
            precision_achieved = True
            break
        
        #Проверяем максимальное количество итераций
        if k >= max_iteration:
            print("-" * 48)
            print(f'Достигнуто максимальное количество итераций ({max_iteration}) за указанное число итераций необходимой точности достичь не удалось')
            break

    if not precision_achieved and k < max_iteration:
        # Выводим последнее состояние если оно не было выведено
        if k % steps != 0:
            print(f'|{k:^10} | {current_number:^15.8f} | {s:^15.8f}|')
        print("-" * 48)

    #Вывод
    print(f"Сумма бесконечного ряда - {4*s:.10f} вычислена за {k} итераций")
    