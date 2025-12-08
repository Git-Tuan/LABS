# ИУ7-14Б, Дао Ань Туан, лаба 13

import os

filename = input('Введите путь к файлу: ')

CHUNK_SIZE = 100   # сколько строк читаем за раз


def parse_line(line):
    """Разбивает строку на поля по разделителю | и убирает пробелы."""
    return [col.strip() for col in line.strip().split("|")]

def to_number(val):
    """Преобразует строку в число (int или float), если возможно, иначе оставляет строкой."""
    val = val.strip()
    try:
        return int(val)
    except ValueError:
        try:
            return float(val)
        except ValueError:
            return val  # оставить строкой


def compare_key(fields, sort_fields):
    """
    Возвращает ключ сортировки.
    args:
        sort_fields(list): список индексов полей, по которым сортируем, например [0] или [0,2]
        fields(list): список значений строки
    """
    key = []
    for idx in sort_fields:
        val = fields[idx]
        # Преобразуем к числу, если возможно, иначе оставляем строкой
        key.append(to_number(val))
    return tuple(key)


def create_sorted_blocks(path, sort_fields):
    """Делит файл на множество подфайлов
        args: 
            path(str): путь до исходного файла
            sort_fields(list): список, состоящий из индексов столбцов, требующих сортировку
        return:
            header(str): поля бд
            block_files(list): имена временных файлов
    """
    block_files = [] # Список, хранящий имена временных файлов
    chunk = [] # Список, хранящий еще неотсортированные строки из исходной бд
    block_index = 0 # Индекс временного файла

    with open(path, "r", encoding='UTF-8') as f:
        header = f.readline()  # читаем заголовок, сохраняем как есть

        for line in f: 
            chunk.append(line)

            if len(chunk) == CHUNK_SIZE:
                block_name = f"block_{block_index}.tmp"
                block_index += 1

                chunk = sort_chunk(chunk, sort_fields) # Сортируем "кусок" базы данных
                write_block(block_name, chunk) # Во временный файл уже записываем отсортированные строки бд

                block_files.append(block_name)
                chunk = []

        # Последний хвост
        if chunk:
            block_name = f"block_{block_index}.tmp"
            chunk = sort_chunk(chunk, sort_fields)
            write_block(block_name, chunk)
            block_files.append(block_name)

    return header, block_files


def sort_chunk(chunk, sort_fields):
    """Сортирует одну порцию строк."""
    parsed = [parse_line(line) for line in chunk]
    parsed.sort(key=lambda row: compare_key(row, sort_fields))
    return [" | ".join(row) + "\n" for row in parsed]


def write_block(block_name, chunk):
    """Записывает отсортированный блок во временный файл."""
    with open(block_name, "w", encoding='UTF-8') as bf:
        for line in chunk:
            bf.write(line)


def merge_blocks(header, block_files, output_file):
    """Сливает все временные блоки в один отсортированный файл.
        args:
            header(str): поля бд
            block_files(list): имена файлов
            output_file(str): путь до исходного файла
    """
    # Открываем все временные файлы
    fps = [open(bf, "r", encoding='UTF-8') for bf in block_files]

    # читаем начальные строки
    lines = [fp.readline() for fp in fps]

    with open(output_file, "w", encoding='UTF-8') as out:
        out.write(header)  # сначала заголовок

        while True:
            # убираем законченные файлы
            active = [(i, line) for i, line in enumerate(lines) if line]

            if not active:
                break

            # выбираем строку с минимальным ключом
            min_index = min(
                active,
                key=lambda x: compare_key(parse_line(x[1]), sort_fields_for_merge)
            )[0]

            out.write(lines[min_index])

            # читаем след. строку из того же файла
            lines[min_index] = fps[min_index].readline()

    # закрываем и удаляем временные файлы
    for fp, fname in zip(fps, block_files):
        fp.close()
        os.remove(fname)


def external_sort(path, sort_fields):
    """
    sort_fields — список полей, по которым сортируем.
    Например:
        [0] — сортировка по 1 полю
        [1, 0] — сортировка по 2 полям
    """
    global sort_fields_for_merge
    sort_fields_for_merge = sort_fields  # сохраняем глобально для merge()

    header, block_files = create_sorted_blocks(path, sort_fields)

    output_file = path  # сортировка перезаписывает исходный файл

    merge_blocks(header, block_files, output_file)

    print("Файл успешно отсортирован!")

def verify_path(path):
    exists = False
    try:
        with open(path) as f:
            return True
    except FileNotFoundError:
        pass
    return exists


def print_file(path):
    print('Содержимое файла:\n')
    with open(path, 'r', encoding='UTF-8') as f:
        for line in f:
            print('-' * 63)
            output = ''
            line = line.strip()   
            cols = line.split('|')   
            for col in cols:
                output += f'{col.strip():^20}|'  
            print(output)

def add_record(path):
    """Добавление новой записи в конец файла."""
    with open(path, 'r', encoding='UTF-8') as f:
        header = f.readline().strip().split('|')
    length = len(header)

    values = input(f'Введите {length} значений через пробел: ').split()
    if len(values) != length:
        print('Ошибка: неправильное число полей.')
        return

    with open(path, 'a', encoding='UTF-8') as f:
        f.write(' | '.join(values) + '\n')

    print('Запись успешно добавлена!')


def search_one(path):
    """Поиск по одному полю (по первому)."""
    key = input('Введите значение для поиска по первому полю: ').strip()

    with open(path, 'r', encoding='UTF-8') as f:
        for line in f:
            cols = [c.strip() for c in line.strip().split('|')]
            if cols[0] == key:
                print('Найдено:', cols)


def search_two(path):
    """Поиск по первым двум полям."""
    key1 = input('Введите значение для поиска по первому полю: ').strip()
    key2 = input('Введите значение для поиска по второму полю: ').strip()

    with open(path, 'r', encoding='UTF-8') as f:
        for line in f:
            cols = [c.strip() for c in line.strip().split('|')]
            if len(cols) >= 2 and cols[0] == key1 and cols[1] == key2:
                print('Найдено:', cols)
            

def menu(path):
    """Главное меню программы."""
    while True:
        print("\nМеню:")
        print("1 — Показать содержимое файла")
        print("2 — Добавить запись")
        print("3 — Поиск по одному полю")
        print("4 — Поиск по двум полям")
        print("5 - Упорядочить по одному полю")
        print("6 - Упорядочить по двум полям")  
        print("0 — Выход")

        choice = input("Ваш выбор: ")

        if choice == '1':
            print_file(path)
        elif choice == '2':
            add_record(path)
        elif choice == '3':
            search_one(path)
        elif choice == '4':
            search_two(path)
        elif choice == '5':
            field = int(input("Введите номер поля (начиная с 1): ")) - 1
            external_sort(filename, [field])
        elif choice == '6':
            f1 = int(input("Введите номер первого поля: ")) - 1
            f2 = int(input("Введите номер второго поля: ")) - 1
            external_sort(filename, [f1, f2])
        elif choice == '0':
            print("Выход из программы.")
            break
        else:
            print("Неверный пункт меню!")


if verify_path(filename):
    print("Файл найден.")
    menu(filename)

else:
    response = input('Файл не существует, хотите создать новый файл? Y / N > ').lower()
    while response != 'y' and response != 'n':
        response = input('Некоректный ввод, ожидаем ответа (Y / N) > ').lower()
      
        
    if response == 'y':
        path = input('Введите новый путь к файлу: ')
        try:
            with open(path, 'w', encoding='UTF-8') as new_file:
                num_of_rows = int(input('Введите кол-во записей: '))
                cols = input('Введите поля для инициализации базы данных через |: ').split('|')
                length = len(cols)
                new_file.write(' | '.join(cols) + '\n')
               
                k = 0
                while k < num_of_rows:
                    line = input('Введите запись бд через пробел: ').split()
                    if len(line) == length:
                        new_file.write(' | '.join(line) + '\n')
                        print('Успешная запись!')
                        k += 1
                    else:
                        print(f'Неправильный ввод. Вам необходимо ввести {length} элементов. Повторите попытку') 

            print_file(path)
            menu(path)
                
        except FileNotFoundError:
            print('Файл не может быть создан. Выход из программы')
        
        
    else:
        print('Выход из программы')
