# Дао Ань Туан ИУ7И-14Б, Задание 1, наибольшее кол-во идущих подряд одинаковых элементов
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
        mod1.print_matrix(matrix)

        # Поиск строки с максимальной последовательностью одинаковых элементов
        max_similar = 0
        index = -1

        for row in range(len(matrix)):
            current_count = 1
            max_in_row = 1
            
            # Проходим по всем элементам строки, начиная со второго
            for col in range(1, len(matrix[row])):
                if matrix[row][col] == matrix[row][col - 1]:
                    current_count += 1
                    # Обновляем максимум для текущей строки
                    if current_count > max_in_row:
                        max_in_row = current_count
                else:
                    current_count = 1  # Сбрасываем счетчик при изменении элемента
            
            # Проверяем, является ли эта строка лучшей
            if max_in_row > max_similar:
                max_similar = max_in_row
                index = row

        # Вывод результата
        if index != -1 and max_similar > 1:
            print(f'\nСтрока № {index + 1} имеет наибольшее кол-во повторяющихся элементов подряд: {max_similar}')
            print('Элементы строки:', *matrix[index])
        else:
            print('\nВ матрице нет последовательностей одинаковых элементов длиной больше 1')

    else:
        print('Неправильно введены rows и columns')
        exit()
else:
    print('Неправильно введены rows и columns')



