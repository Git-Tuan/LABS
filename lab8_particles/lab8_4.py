# Дао Ань Туан ИУ7И-14Б
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
        print('Исходная матрица: ')
        for i in matrix:
            print('|', end='')
            for j in i:
                print(f'{j:^12}|', end='')
            print()  


        # Поиск столбца с наибольшим количеством нулевых элементов
        max_sum = -float('inf')
        min_sum = float('inf')
        mx_col_index = -1
        mn_col_index = -1
        
        # Перебор по столбцам
        for col in range(int(columns)):
            summation = 0
            # По строкам
            for row in range(int(rows)):
                summation += int(matrix[row][col])
            # Максимальная сумма
            if summation > max_sum:
                max_sum = summation
                mx_col_index = col
            # Минимальная сумма
            if summation < min_sum:
                min_sum = summation
                mn_col_index = col

        # Перестановка столбцов   
        for row in range(len(matrix)):
            if mx_col_index != mn_col_index:
                matrix[row][mx_col_index], matrix[row][mn_col_index] = matrix[row][mn_col_index], matrix[row][mx_col_index]
                print('Матрица после перестановки строк:')
                mod1.print_matrix(matrix)
            else:
                print('Матрица не изменена')
else:
    print('Неправильно введены rows и columns')