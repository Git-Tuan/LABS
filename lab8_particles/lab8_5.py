# Дао Ань Туан ИУ7И-14Б, Задание 5
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
            mod1.print_matrix(matrix)


            max_val = -float('inf')
            min_val = float('inf')
            # Ищем максимальное значение над главной диагональю
            for row in range(int(rows)):
                # Перебираем по столбцам, справа налево до значений, лежащих на диагонали невключительно
                for i in range(int(rows)-1, row, -1):
                    if int(matrix[row][i]) > max_val:
                        max_val = int(matrix[row][i])
            

            # Ищем минимальное значение под побочной диагональю
            # Перебираем строки справа налево
            for row in range(int(rows)-1, -1, -1):
                for i in range(int(rows)-1, int(rows)-row-1, -1):
                    if int(matrix[row][i]) < min_val:
                        min_val = int(matrix[row][i])
        

            print('Максимум над главной диагональю: ', max_val)
            print('Минимум под побочной диагональю:  ', min_val)
    else:
        print('Матрица не квадратная')
else:
    print('Неправильно введены rows и columns')


