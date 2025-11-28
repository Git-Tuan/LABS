def check_rows_col(rows, columns):
    if rows == '' or columns == '':
        return False
    
    # Проверка rows
    is_rows_int = True
    for char in rows:
        if char not in '0123456789':
            is_rows_int = False
            break

    if not is_rows_int:
        return False

    # Проверка columns
    is_columns_int = True
    for char in columns:
        if char not in '0123456789':
            is_columns_int = False
            break

    if not is_columns_int:
        return False
    
    # Проверка что числа не равны 0
    if int(rows) == 0 or int(columns) == 0:
        return False
        
    return True


def check_values(user_input, columns):
    # Проверка количества элементов
    if len(user_input) != int(columns):
        return False
    
    row = []
    
    # Перебор элементов строки
    for element in user_input:
        dot_count = 0
        digit_count = 0
        has_minus = False
        
        # Перебираем символы в каждом элементе
        for char_idx, char in enumerate(element):
            if char == '-':
                if char_idx == 0:  # Минус может быть только в начале
                    has_minus = True
                else:
                    return False
                    
            elif char == '.':
                # Число не является типом float
                return False
                    
            elif char in '0123456789':
                digit_count += 1
                
            else:
                return False
        
        # Финальные проверки
        if digit_count == 0:
            return False
            
        # Проверка на случай только минуса
        if has_minus and len(element) == 1:
            return False
        

        
        row.append(element)
    
    return row


def print_matrix(matrix):
    for i in matrix:
        print('|', end='')
        for j in i:
            print(f'{j:^12}|', end='')
        print()


