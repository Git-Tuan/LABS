# Дао Ань Туан, ИУ7И-14Б, задание 3
import mod1 

rows = input('Введите кол-во строк для 1-ой матрицы: ')
rows2 = input('Введите кол-во строк для 2-ой матрицы: ')
columns = input('Введите кол-во столбцов для обеих матриц: ')
if mod1.check_rows_col(rows) and mod1.check_rows_col(rows2):
    rows = int(rows)
    rows2 = int(rows2)
    columns = int(columns)
    A = []
    B = []
    average = []
    # Создание матрицы A
    for i in range(rows):
        user_input = input(f'Введите элементы {i+1} строки для 1-ой матрицы: ').split()
        if mod1.check_values(user_input): 
            A.append(list(map(int, user_input)))
        else:
            print('Ошибка, не удалось добавить числа в матрицу. Перепроверьте корректность данных')
            exit()
    # Создание матрицы B
    for i in range(rows2):
        user_input = input(f'Введите элементы {i+1} строки для 2-ой матрицы: ').split()
        if mod1.check_values(user_input): 
            B.append(list(map(int, user_input)))
        else:
            print('Ошибка, не удалось добавить числа в матрицу. Перепроверьте корректность данных')
            exit()
    
    print("\nИсходные матрицы:")
    for row in mod1.print_matrix(A):
        print(row)
    print()
    for row in mod1.print_matrix(B):
        print(row)

    # Вычисление средних арифметических значений для каждого столбца, их сохранение для последующего вывода
    for i_col in range(columns):
        s = 0
        for i_row in range(rows2):
            s += B[i_row][i_col]
        average.append(s//columns)

   # Количество элементов, больших среднего арифметического элементов соответствующего столбца матрицы В
    for i_col in range(columns):
        count = 0
        for i_row in range(rows):
            if A[i_row][i_col] > average[i_col]:
                count += 1
        average[i_col] = count
        
    
    for i_col in range(columns):
        if average[i_col] != 0:
            for i_row in range(rows2):
                B[i_row][i_col] = B[i_row][i_col] * average[i_col]
        
    for line in mod1.print_matrix(B):
        print(line)

