# Дао Ань Туан, ИУ7И-14Б, задание 3
import mod1 

rows = input('Введите кол-во строк(столбцов) для матрицы: ')
columns = rows
matrix = []
if mod1.check_rows_col(rows):
    rows = int(rows)
    columns = int(columns)
    # Создание матрицы 
    for i in range(rows):
        user_input = input(f'Введите элементы {i+1} строки для 1-ой матрицы: ').split()
        if mod1.check_values(user_input): 
            matrix.append(list(map(int, user_input)))
        else:
            print('Ошибка, не удалось добавить числа в матрицу. Перепроверьте корректность данных')
            exit()


print("Исходная матрица:")
for i in mod1.print_matrix(matrix):
    print(i)

l, r = 0, len(matrix) - 1

while l < r:
    # Начинаем циклическую перестановку
    # Перемещаем левый нижний элемент на место правого верхнего
    for i in range(r-l):
        top, bot = l, r
        temp = matrix[top][l+i]
        matrix[top][l+i] = matrix[bot-i][l]
        matrix[bot-i][l] = matrix[bot][r-i]
        matrix[bot][r-i] = matrix[top+i][r]
        matrix[top+i][r] = temp
    
    l += 1
    r -= 1
print()
for line in mod1.print_matrix(matrix=matrix):
    print(line)
l, r = 0, len(matrix) - 1

while l < r:
    for i in range(r-l):
        top, bot = l, r
        temp = matrix[bot][r-i]
        matrix[bot][r-i] = matrix[bot-i][l]
        matrix[bot-i][l] = matrix[top][l+i]
        matrix[top][l+i] = matrix[top+i][r]
        matrix[top+i][r] = temp

    l += 1
    r -= 1

print()
for line in mod1.print_matrix(matrix=matrix):
    print(line)