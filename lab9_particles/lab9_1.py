# Дао Ань Туан, ИУ7И-14Б, задание 1
import mod1 
# Ввод данных, элементы двух списков
a = input('Введите числа через пробел: ').split()
b = input('Снова введите числа через пробел для заполнения второго массива: ').split()

# Если введенные значения правильные
if mod1.check_values(a) and mod1.check_values(b) and a and b:
    a = list(map(int, a))
    b = list(map(int, b))
    matrix = []
    S = []
    # Формирование матрицы двумя списками
    for row in range(len(a)):
        # Строка матрицы
        cur_row = []
        for col in range(len(b)):
            cur_row.append(a[row]*b[col])
        matrix.append(cur_row)


    count = 0
    # Нахожднение полных квадратов в матрице, добавление их кол-ва в 1-ой строке в S
    for row in matrix:
        for element in row:
            if element >= 0:
                root = element**0.5
                if root*root == element:
                    count += 1
        S.append(count)
        count = 0

    # Печатаем матрицу и кол-во полных квадратов в каждой строке
    for row in mod1.print_matrix(matrix=matrix):
        print(row, S[count])
        count += 1
else:
    print('Ошибка. Были введены неправильные значения')


