def check_rows_col(rows_or_col):
    condition = True
    if rows_or_col == '' or float(rows_or_col) == 0.0:
        condition = False

    if condition:
        for char in rows_or_col:
            if char not in '0123456789':
                condition = False
                break

    return condition


def check_values(row):
    condition = True
    # Перебор элементов строки
    for element in row:
        digit_count = 0
        has_minus = False
        
        # Перебираем символы в каждом элементе
        for char_idx, char in enumerate(element):
            if char == '-':
                if char_idx != 0:  # Минус может быть только в начале
                    condition = False
                    break
        
            elif char == '.':
                # Число не является типом float
                condition = False
                break
                    
            elif char in '0123456789':
                digit_count += 1
                
            else:
                condition = False
                break
            
        # Проверка на случай только минуса
        if has_minus and len(element) == 1:
            condition = False

    return condition 


def print_matrix(matrix):
    rows = []
    for row in matrix:
        string = ''
        string += ('|')
        for col in row:
            string += f'{col:^12}'
        string += ('|')
        rows.append(string)
    return rows


