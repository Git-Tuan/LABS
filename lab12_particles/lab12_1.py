text = ['          Я лгать не хотел в этом даже себе! Не для того, чтобы матери помочь, я убил — вздор!',
            '      Не для того я убил, чтобы, получив средства и власть, сделаться благодетелем человечества.              ',
            '                    Вздор! Я просто убил; для себя убил, для себя одного: а там стал ли бы я чьим-нибудь благодетелем или всю жизнь,',
            '         как паук, ловил бы всех в паутину и из всех живые соки высасывал, мне, в ту минуту, всё равно должно было быть!.. ',
            'И не деньги, главное, нужны мне были, Соня, когда я убил; не столько деньги нужны были, как другое… '
            'Мне другое надо было узнать, другое толкало меня под руки: мне надо было узнать тогда, и поскорей узнать, вошь ли я, как все, или человек?',
            '                      Смогу ли я переступить или не смогу! Осмелюсь ли нагнуться и взять или нет? Тварь ли я дрожащая или право имею…']


def print_text():
    """Вывод текста построчно"""
    print('\nИсходный текст:')
    for line in text:
        print(line)
    print()

def max_line_length():
    """Возвращает длину самой длинной строки"""
    return max(len(line) for line in text)

def align_left():
    """Выровнять по левому краю — фактически убрать лишние пробелы"""
    global text
    new_text = []
    for line in text:
        words = line.split()
        new_text.append(' '.join(words))
    text = new_text

def align_right():
    """Выровнять текст по правому краю"""
    global text
    width = max_line_length()
    new_text = []
    for line in text:
        stripped = ' '.join(line.split())
        spaces = width - len(stripped)
        new_text.append(' ' * spaces + stripped)
    text = new_text

def align_width():
    """Выровнять текст по ширине"""
    global text
    width = max_line_length()
    new_text = []

    for line in text:
        words = line.split()
        if len(words) == 1:
            # Одно слово не растягиваем
            new_text.append(words[0])
            continue

        total_chars = sum(len(w) for w in words)
        spaces_total = width - total_chars
        gaps = len(words) - 1

        # равномерное распределение пробелов
        base_spaces = spaces_total // gaps
        extra_spaces = spaces_total % gaps

        new_line = ''
        for i, w in enumerate(words):
            new_line += w
            if i < gaps:
                # распределяем 'лишние' пробелы по одному слева
                spaces = base_spaces + (1 if i < extra_spaces else 0)
                new_line += ' ' * spaces

        new_text.append(new_line)

    text = new_text



def menu():
    while True:
        print('''
            МЕНЮ:
            1 — Выровнять текст по левому краю
            2 — Выровнять текст по правому краю
            3 — Выровнять текст по ширине
            4 — Показать текст
            0 — Выход
            ''')

        choice = input('Выберите пункт меню: ')

        if choice == '1':
            align_left()
            print('Текст выровнен по левому краю.')
        elif choice == '2':
            align_right()
            print('Текст выровнен по правому краю.')
        elif choice == '3':
            align_width()
            print('Текст выровнен по ширине.')
        elif choice == '4':
            print_text()
        elif choice == '0':
            print('Выход.')
            break
        else:
            print('Неверный ввод. Повторите.')

menu()
