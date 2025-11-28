# Дао Ань Туан, ИУ7И-14Б, задание 5, произведение матрицы
import mod1 

# Ввод данных, кол-во столбцов и строк матрицы
rows = input('Введите кол-во строк для 1-ой матрицы: ')
rows2 = input('Введите кол-во строк для 2-ой матрицы: ')
columns = input('Введите кол-во столбцов для 1-ой матрицы: ')
columns2 = input('Введите кол-во столбцов для 2-ой матрицы: ')
# Проверяет корректность данных
if mod1.check_rows_col(rows) and mod1.check_rows_col(rows2) and mod1.check_rows_col(columns2) and mod1.check_rows_col(columns):
    rows, rows2, columns, columns2 = int(rows), int(rows2), int(columns), int(columns2)
    A = []
    B = []
    # Создание матрицы
    for i in range(rows):
        user_input = input(f'Введите элементы {i+1} строки для 1-ой матрицы: ').split()
        if mod1.check_values(user_input) and len(user_input) == columns: 
            A.append(list(map(int, user_input)))
        else:
            print('Ошибка, не удалось добавить числа в матрицу. Перепроверьте корректность данных')
            exit()
    # Создание матрицы
    for i in range(rows2):
        user_input = input(f'Введите элементы {i+1} строки для 2-ой матрицы: ').split()
        if mod1.check_values(user_input) and len(user_input) == columns2: 
            B.append(list(map(int, user_input)))
        else:
            print('Ошибка, не удалось добавить числа в матрицу. Перепроверьте корректность данных')
            exit()
    # Вывод матриц
    for a in mod1.print_matrix(A):
        print(a)
    for b in mod1.print_matrix(B):
        print(b)

    # Умножение матриц, через динамику
    C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
        
    if rows == rows2:
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    C[i][j] += A[i][k]* B[k][j]
    # Вывод матрицы C              
    for c in mod1.print_matrix(C):
        print(c)
