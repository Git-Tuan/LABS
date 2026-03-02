# Дао Ань Туан, ИУ7-24Б
# Сложение, вычитание и умножение вещественных чисел в 2-й 
# системе счисления.  
'''
def toBinary(num: int):
    res = ''
    if type(num) == int:
        while num > 0:
            res = str(num % 2) + res
            num //= 2
    else:
        dotPos = str(num).index('.')
        integerPart = int(str(num)[:dotPos])
        #i = 0
        while integerPart > 0:
            res = str(integerPart % 2) + res
            integerPart //= 2
            #i += 1

        res += '.'
        fraction = float('0'+ str(num)[dotPos:])
        length = len(str(num)[dotPos:]) - 1
        strFraction = str(fraction)
        attempt = 0

        while attempt < length:
            res = res + str(fraction * 2)[0]
            strFraction = str(fraction * 2)
            fraction = float('0' + strFraction[strFraction.index('.'):])
            attempt += 1

    return res


def toDecimal(num: str):
    i = 0
    res = 0
    dotPos = None
    for j in range(len(num)):
        if num[j] == '.': dotPos = j

    if not dotPos:
        while i < len(num):
            if num[i] == '1':
                res += 2**(len(num)-1-i)
            
            i += 1

        return res
    else:
        while i < dotPos:
            if num[i] == '1':
                res += 2**(dotPos-1-i)

            i += 1
        
        #i = -1

        for j in range(dotPos+1, len(num)):
            if num[j] == '1':
                res += 2**(dotPos-j)
        return res
'''



DIGITS = "0123456789ABCDEF"

def normalize(a, b):
    a = a.upper()
    b = b.upper()
    
    if '.' not in a:
        a += '.'
    if '.' not in b:
        b += '.'
    
    int_a, frac_a = a.split('.')
    int_b, frac_b = b.split('.')
    

    max_frac = max(len(frac_a), len(frac_b))
    frac_a += '0' * (max_frac - len(frac_a))
    frac_b += '0' * (max_frac - len(frac_b))
    
    max_int = max(len(int_a), len(int_b))
    int_a = '0' * (max_int - len(int_a)) + int_a
    int_b = '0' * (max_int - len(int_b)) + int_b
    
    return int_a + frac_a, int_b + frac_b, max_frac


def add_numbers(a, b, base):
    a, b, frac_len = normalize(a, b)
    
    a = a[::-1]
    b = b[::-1]
    
    carry = 0
    result = ""
    
    for i in range(len(a)):
        digit_a = DIGITS.index(a[i])
        digit_b = DIGITS.index(b[i])
        
        total = digit_a + digit_b + carry
        result += DIGITS[total % base]
        carry = total // base
    
    if carry:
        result += DIGITS[carry]
    
    result = result[::-1]
    
    if frac_len:
        result = result[:-frac_len] + '.' + result[-frac_len:]
    
    result = result.rstrip('0').rstrip('.') or '0'
    return result


def subtract_numbers(a, b, base):
    a, b, frac_len = normalize(a, b)
    a = a[::-1]
    b = b[::-1]
    
    result = ""
    borrow = 0
    
    for i in range(len(a)):
        digit_a = DIGITS.index(a[i])
        digit_b = DIGITS.index(b[i])
        
        diff = digit_a - digit_b - borrow
        
        if diff >= 0:
            result += DIGITS[diff]
            borrow = 0
        else:
            result += DIGITS[diff + base]
            borrow = 1
    
    result = result[::-1]
    
    if frac_len:
        result = result[:-frac_len] + '.' + result[-frac_len:]
    
    result = result.lstrip('0')
    if result[0] == '.':
        result = '0' + result

    result = result.rstrip('0').rstrip('.') or '0'

    return result

def multiply_numbers(a, b, base):
    a_norm, b_norm, frac_len = normalize(a, b)
    
    total_frac = frac_len * 2
    
    result = "0"
    b_norm = b_norm[::-1]
    
    for i in range(len(b_norm)):
        digit_b = DIGITS.index(b_norm[i])
        temp = ""
        carry = 0
        
        for digit_a_char in reversed(a_norm):
            digit_a = DIGITS.index(digit_a_char)
            product = digit_a * digit_b + carry
            
            temp += DIGITS[product % base]
            carry = product // base
        
        if carry:
            temp += DIGITS[carry]
        
        temp = temp[::-1] + "0" * i
        result = add_numbers(result, temp, base).replace('.', '')
    
    if total_frac:
        result = result[:-total_frac] + '.' + result[-total_frac:]
    
    result = result.rstrip('0').rstrip('0') or '0'
    return result

def calculate(expression: str):
    op_idx = -1
    expression = expression if '=' not in expression else expression[:len(expression)-1]
    for i in range(len(expression)):
        if expression[i] in '-*+': 
            op_idx = i
            break
        else: continue
    
    print(op_idx)

    if op_idx == -1 or op_idx == len(expression) - 1:
        pass

    else:  
        num1 = expression[:op_idx]
        num2 = expression[op_idx+1:]
        #if ns == 'BIN': 
        #    num1, num2 = toDecimal(str(num1)), toDecimal(str(num2))
        operator = expression[op_idx]
        
        if operator == '+':
            res = add_numbers(num1, num2, 2)
        elif operator == '-':
            res = subtract_numbers(num1, num2, 2)
        elif operator == '*':
            res = multiply_numbers(num1, num2, 2)
        else:
            res = 0
        
        return res
