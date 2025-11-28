# Дао Ань Туан, ИУ7И-14Б, задание 4
import mod1
# Инициализация строк и столбцов матрицы
rows = input('Введите кол-во строк(столбцов) для матрицы: ')
columns = input('Введите кол-во столбцов для матрицы: ')
# Проверка корректности данных
if mod1.check_rows_col(rows) and mod1.check_rows_col(columns):
    D = []
    I = []
    R = []
    # Создание матрицы D
    for i in range(int(rows)):
        user_input = input(f'Введите элементы {i+1} строки через пробел: ').split()
        if mod1.check_values(user_input): 
            D.append(user_input)
        else:
            print('Ошибка, не удалось добавить числа в матрицу. Перепроверьте корректность данных')
            exit()

    # Ввод номера строки, в которой будет искаться максимум, запоминаем в I
    user_input = input('Введите строки, в которых необходимо определить максимальное значение через пробел: ').split()
    # Проверка корректности данных, номера не должны превышать кол-во строк или быть отрицательными
    if mod1.check_values(user_input):
        for i_col in user_input:
            if 0 < int(i_col) <= int(rows):
                I.append(int(i_col)-1)
            else:
                print('Введеннные значения превышают кол-во строк матрицы')
                exit()
        print(D)
        print(I)

        # Ищем максимум в каждой строке, запоминаем в R
        for i_row in I:
            max_in_row = float('-inf')
            for element in D[i_row]:
                if int(element) > max_in_row:
                    max_in_row = int(element)
            R.append(max_in_row)

        print(R)
        # Находим среднее арифметическое
        s = 0
        for num in R:
            s += num
        if len(R) != 0:
            print(s//len(R))
        
        




            
