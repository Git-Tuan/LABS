import os
import struct

# 2 целых числа + 2 текстовых поля по 20 байт
RECORD_STRUCT = struct.Struct("ii20s20s")
RECORD_SIZE = RECORD_STRUCT.size



def encode_field(s, size=20):
    """Преобразование строки в байты фиксированной длины."""
    return s.encode('utf-8')[:size].ljust(size, b'\x00')


def decode_field(b):
    """Преобразование байтового поля в строку."""
    return b.decode('utf-8', errors='ignore').rstrip('\x00')


def read_record(f, index):
    """Считать одну запись по индексу (0-based)."""
    f.seek(index * RECORD_SIZE)
    data = f.read(RECORD_SIZE)
    if len(data) < RECORD_SIZE:
        return None
    id_, age, name, city = RECORD_STRUCT.unpack(data)
    return [id_, age, decode_field(name), decode_field(city)]


def write_record(f, index, rec):
    """Записать запись по индексу."""
    id_, age, name, city = rec
    packed = RECORD_STRUCT.pack(
        id_,
        age,
        encode_field(name),
        encode_field(city)
    )
    f.seek(index * RECORD_SIZE)
    f.write(packed)


def record_count(path):
    """Кол-во записей в бинарном файле."""
    size = os.path.getsize(path)
    return size // RECORD_SIZE


def print_record_as_table(rec):
    """Вывод одной записи в формате таблицы."""
    width = 20
    print("-" * (width * len(rec) + len(rec) + 1))
    row = ""
    for col in rec:
        row += f"{str(col).strip():^{width}}|"
    print(row)


def print_file(path):
    print("\nСодержимое бинарной базы:\n")
    with open(path, "rb") as f:
        n = record_count(path)
        for i in range(n):
            rec = read_record(f, i)
            if rec:
                print_record_as_table(rec)


def add_record(path):
    print("Введите запись как: id age name city")
    parts = input().split()

    if len(parts) != 4:
        print("Ошибка: нужно 4 поля")
        return

    id_, age = int(parts[0]), int(parts[1])
    name, city = parts[2], parts[3]

    with open(path, "ab") as f:
        packed = RECORD_STRUCT.pack(
            id_, age, encode_field(name), encode_field(city)
        )
        f.write(packed)

    print("Запись добавлена.")



def search_one(path):
    key = int(input("Введите id: "))
    with open(path, "rb") as f:
        n = record_count(path)
        for i in range(n):
            rec = read_record(f, i)
            if rec[0] == key:
                print("Найдено:", rec)


def search_two(path):
    key1 = int(input("Введите id: "))
    key2 = int(input("Введите age: "))

    with open(path, "rb") as f:
        n = record_count(path)
        for i in range(n):
            rec = read_record(f, i)
            if rec[0] == key1 and rec[1] == key2:
                print("Найдено:", rec)



def insert_record(path):
    pos = int(input("Введите позицию вставки: "))
    print("Введите запись (id age name city):")
    parts = input().split()

    id_, age = int(parts[0]), int(parts[1])
    name, city = parts[2], parts[3]

    newrec = RECORD_STRUCT.pack(
        id_, age, encode_field(name), encode_field(city)
    )

    with open(path, "rb+") as f:
        n = record_count(path)

        if pos < 0 or pos > n:
            print("Некорректная позиция")
            return

        # Расширяем файл на 1 запись
        f.seek(n * RECORD_SIZE)
        f.write(b"\x00" * RECORD_SIZE)

        # Сдвигаем записи вниз
        for i in range(n, pos, -1):
            prev = read_record(f, i - 1)
            write_record(f, i, prev)

        # Записываем новую
        write_record(f, pos, [id_, age, name, city])

    print("Запись вставлена.")



def remove_record(path):
    pos = int(input("Введите номер удаляемой записи: "))

    with open(path, "rb+") as f:
        n = record_count(path)
        if pos < 0 or pos >= n:
            print("Некорректный номер")
            return

        # Сдвигаем записи вверх
        for i in range(pos, n - 1):
            nxt = read_record(f, i + 1)
            write_record(f, i, nxt)

        # Укорачиваем файл
        f.truncate((n - 1) * RECORD_SIZE)

    print("Запись удалена.")


def menu(path):
    while True:
        print("\nМеню:")
        print("1 — показать содержимое")
        print("2 — добавить запись")
        print("3 — поиск по одному полю")
        print("4 — поиск по двум полям")
        print("5 — вставить запись")
        print("6 — удалить запись")
        print("0 — выход")

        c = input("Ваш выбор: ")

        if c == "1": print_file(path)
        elif c == "2": add_record(path)
        elif c == "3": search_one(path)
        elif c == "4": search_two(path)
        elif c == "5": insert_record(path)
        elif c == "6": remove_record(path)
        elif c == "0": break



filename = input("Введите путь к бинарному файлу: ")

if not os.path.exists(filename):
    print("Файл не найден. Создаю новый.")
    open(filename, "wb").close()

menu(filename)
