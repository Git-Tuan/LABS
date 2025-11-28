# Дао Ань Туан, ИУ7И-14Б, задание 6
import mod1

# Ввод данных, столбцы, строки матрицы
rows = input('Введите кол-во строк(столбцов) для матрицы: ')
columns = input('Введите кол-во строк(столбцов) для матрицы: ')
alphabet = 'qwertyuiopasdfghjklzxcvbnm'
matrix = []
# Проверка корректности данных
if mod1.check_rows_col(rows) and mod1.check_rows_col(columns):
    rows = int(rows)
    columns = int(columns)
    # Создание матрицы 
    for i_row in range(rows):
        user_input = input('Введите латинские буквы через пробел: ').split()
        if len(user_input) == columns:
            # Проверяем, что все значения - буквы
            for word in user_input:
                if word.lower() not in alphabet:
                    print('Ошибка. Вы ввели не латинскую букву.')
                    exit()

            matrix.append(user_input)
    
        else:
            print('Ошибка. Вы не ввели необходимое кол-во символов')
            exit()
    # Ищем согласные и гласные в матрице, согласные становятся заглавными, гласные - строчными
    '''for i_row in range(rows):
        for i_col in range(columns):
            for i_let in range(len(matrix[i_row][i_col])):
                if matrix[i_row][i_col][i_let] in 'qwrtpsdfghjklzxcvbnm':
                    matrix[i_row][i_col] = matrix[i_row][i_col].replace(matrix[i_row][i_col][i_let], matrix[i_row][i_col][i_let].upper())
                elif matrix[i_row][i_col][i_let] in 'EYUIOA':
                    matrix[i_row][i_col] = matrix[i_row][i_col].replace(matrix[i_row][i_col][i_let], matrix[i_row][i_col][i_let].lower())'''
    
    for i_row in range(rows):
        for i_col in range(columns):
            if matrix[i_row][i_col] in 'qwrtpsdfghjklzxcvbnm':
                matrix[i_row][i_col] = matrix[i_row][i_col].upper()
            elif matrix[i_row][i_col] in 'EYUIOA':
                matrix[i_row][i_col] = matrix[i_row][i_col].lower()
    
 

# Вывод матрицы 
for row in mod1.print_matrix(matrix):
    print(row)
                

