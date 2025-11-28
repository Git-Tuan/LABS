# Дао Ань Туан, ИУ7-14Б, задание 7

import mod1 

# Ввод данных
X = input("Введите X (число матриц): ")
Y = input("Введите Y (число строк в каждой матрице): ")
Z = input("Введите Z (число столбцов в строке): ")

if mod1.check_rows_col(X) and mod1.check_rows_col(Y) and mod1.check_rows_col(Z):
    # Преобразование в числа
    X = int(X)
    Y = int(Y)
    Z = int(Z)
    
    # Создание трёхмерного массива
    array_3d = []
    for x in range(X):
        print(f"\nСлой {x+1}:")
        layer = []
        for y in range(Y):
            row = input(f'Введите элементы {y+1} строки через пробел: ').split()
            if mod1.check_values(row) and len(row) == Z:
                # Преобразуем элементы в числа
                row = [int(element) for element in row]
                layer.append(row)
            else:
                print('Неверные данные для оси Z, невозможна дальнейшая работа программы')
                exit()
        # Добавляем слой в массив
        array_3d.append(layer)

    # Вывод исходного массива
    print("\nИсходный трёхмерный массив:")
    for i, layer in enumerate(array_3d):
        print(f"Слой {i}:")
        for row in layer:
            print(row)
        print()

    # Определяем большее измерение
    if X >= Y and X >= Z:
        max_dim = 0
        max_size = X
    elif Y >= X and Y >= Z:
        max_dim = 1
        max_size = Y
    else:
        max_dim = 2
        max_size = Z

    mid_index = max_size // 2
        
    print(f"Наибольшее измерение: {max_size}")
    print(f"Срез по индексу {mid_index}")

    if max_dim == 0:
        # Срез по X
        print(f"\nСрез по X (слой {mid_index}):")
        for row in array_3d[mid_index]:
            print(row)

    elif max_dim == 1:
        # Срез по Y
        print(f"\nСрез по Y (строка {mid_index} всех слоев):")
        for x in range(X):
            print(f"Слой {x}: {array_3d[x][mid_index]}")

    else:
        # Срез по Z
        print(f"\nСрез по Z (столбец {mid_index} всех строк):")
        for x in range(X):
            print(f"Слой {x}:")
            for y in range(Y):
                print(array_3d[x][y][mid_index], end=" ")
            print()
else:
    print('Были введены неправильные входные данные X,Y,Z')