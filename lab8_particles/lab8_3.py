# Дао Ань Туан ИУ7И-14Б, Задание 3, наибольшее кол-во нулевых элементов
# Ввод кол-ва строк и столбцов матрицы

import mod1
matrix = []
# Проверка rows
rows = input('Введите кол-во строк матрицы: ')
columns = input('Введите кол-во столбцов матрицы: ')

if mod1.check_rows_col(rows, columns):
    for i in range(int(rows)):
        user_input = input(f'Введите элементы {i+1}-й строки матрицы через пробел: ').split()
        checked_row = mod1.check_values(user_input, columns)  # получаем преобразованные числа
        if checked_row:
            matrix.append(checked_row)  # добавляем числа
        
        else:
            print('Неккоректный ввод')
            exit()
    
    if len(matrix) == int(rows):  
        print('Исходная матрица')
        mod1.print_matrix(matrix)

        # Поиск столбца с наибольшим количеством нулевых элементов
        max_zero_count = -1
        max_zero_column = -1

        # Перебор по столбцам
        for col in range(int(columns)):
            zero_count = 0
            for row in range(int(rows)):
                if int(matrix[row][col]) == 0: 
                    zero_count += 1
            # Находим максимальное кол-во нулей
            if max_zero_count == -1 or max_zero_count < zero_count:
                max_zero_count = zero_count
                max_zero_column = col

        # Вывод результата
        if max_zero_count > 0:
            print(f'\nСтолбец {max_zero_column + 1} имеет наибольшее количество нулевых элементов: {max_zero_count}')
            print('Элементы этого столбца:')
            for row in range(int(rows)):
                print(f'{matrix[row][max_zero_column]}')
        else:
            print('\nВ матрице нет нулевых элементов')
else:
    print('Неверно введены rows и columns')