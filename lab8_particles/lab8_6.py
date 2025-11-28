# Дао Ань Туан ИУ7И-14Б, Задание 6
# Ввод кол-ва строк и столбцов матрицы
import mod1
matrix = []
# Проверка rows
rows = input('Введите кол-во строк матрицы: ')
columns = input('Введите кол-во столбцов матрицы: ')

if mod1.check_rows_col(rows, columns):
    if rows == columns:
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
            for i in matrix:
                print('|', end='')
                for j in i:
                    print(f'{j:^12}|', end='')
                print() 


            # Транспонирование квадратной матрицы
            for i in range(int(rows)):
                for j in range(i + 1, int(rows)):  # Обходим только верхний угол матрицы
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

            print('Транспонированная матрица:')
            for row in matrix:
                print('|', end='')
                for col in row:
                    print(f'{col:^12}', '|', end='')
                print()

else:
    print('Неправильно введены rows и columns')
