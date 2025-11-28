# Дао Ань Туан ИУ7И-14Б, Задание 2
# Ввод кол-ва строк и столбцов матрицы
import mod1
matrix = []
# Проверка rows
rows = input('Введите кол-во строк матрицы: ')
columns = input('Введите кол-во столбцов матрицы: ')

if mod1.check_rows_col(rows, columns):
    for i in range(int(rows)):
        user_input = input(f'Введите элементы {i+1}-й строки матрицы через пробел: ').split()
        checked_row = mod1.check_values(user_input, columns)
        if checked_row:
            matrix.append(checked_row)  # добавляем преобразованные числа
        
        else:
            print('Неккоректный ввод')
            exit()

    if len(matrix) == int(rows):  
        mod1.print_matrix(matrix)

        # Индексы строк, имеющих максимальное и минимальное кол-во отрицательных чисел и значения для сравнения
        mx_index, mn_index, max_record, min_record = None, None, -float('inf'), float('inf')
        # Перербор по строкам
        for i in range(len(matrix)):
            count = 0
            # Перебор по столбцам
            for j in range(len(matrix[i])):
                if int(matrix[i][j]) < 0:
                    count += 1

            if mx_index == None or max_record < count:
                mx_index = i
                max_record = count
            if mn_index == None or min_record > count:
                mn_index = i
                min_record = count

        # Перестановка строк
        if mx_index != mn_index:
            matrix[mx_index], matrix[mn_index] = matrix[mn_index], matrix[mx_index]

            print('Матрица после перестановки строк:')
            mod1.print_matrix(matrix)
        else:
            print('Матрица не изменена')
    else:
        print('Неверно')

else:
    print('Неправильно введены rows и columns')
