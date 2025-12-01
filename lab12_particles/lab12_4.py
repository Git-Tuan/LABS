text = ['Я лгать не хотел в этом даже себе! Не для того, чтобы матери помочь, я убил — вздор!',
            'Не для того я убил, чтобы, получив средства и власть, сделаться благодетелем человечества.              ',
            'Вздор! Я просто убил; для себя убил, для себя одного: а там стал ли бы я чьим-нибудь благодетелем или всю жизнь,',
            'как паук, ловил бы всех в паутину и из всех живые соки высасывал, мне, в ту минуту, всё равно должно было быть!.. ',
            'И не деньги, главное, нужны мне были, Соня, когда я убил; не столько деньги нужны были, как другое… '
            'Мне другое надо было узнать, другое толкало меня под руки: мне надо было узнать тогда, и поскорей узнать, вошь ли я, как все, или человек?',
            'Смогу ли я переступить или не смогу! Осмелюсь ли нагнуться и взять или нет? Тварь ли я дрожащая или право имею…']

def delete_word(target):
    global text
    if not target:
        return

    removable = ",;:\"'()[]{}—"  
    end_marks = ".!?" "…"             

    new_text = []

    for line in text:
        words = line.split()
        new_words = []

        for i, token in enumerate(words):
            j = len(token) - 1
            trailing = ""

            # забираем пунктуацию справа
            while j >= 0 and (token[j] in removable or token[j] in end_marks or token[j] == "."):
                trailing = token[j] + trailing
                j -= 1

            core = token[:j+1]

            if core == target:

                transfer = ""

                if len(trailing) >= 3 and trailing[-3:] == "...":
                    transfer = "..."

                elif len(trailing) >= 1:
                    last = trailing[-1]
                    if last == "." or last == "!" or last == "?" or last == "…":
                        transfer = last

                if transfer != "" and i == len(words) - 1:
                    if len(new_words) > 0:
                        new_words[-1] = new_words[-1] + transfer
                    else:
                        new_words.append(transfer)

                continue

            new_words.append(token)

        new_line = " ".join(new_words)
        new_text.append(new_line)

    text = new_text


def print_text():
    """Вывод текста построчно"""
    print('\nИсходный текст:')
    for line in text:
        print(line)
    print()             

def replace_word(word_to_replace, new_word):
    global text
    w1 = word_to_replace.strip()
    w2 = new_word.strip()

    new_text = []
    for line in text:
        words = line.split()
        replaced = [w2 if w == w1 else w for w in words]
        new_text.append(" ".join(replaced))
    text = new_text


def main():
    while True:
        print()
        print('\tМЕНЮ:')
        print('''
        1 - удалить слово
        2 - заменить слово
        3 - вывести текст
        0 - выйти''')
        user_input = input('> ')
        if user_input == '1':
            word_to_remove = input('Какое слово хотите удалить? ')
            delete_word(word_to_remove)
        elif user_input == '2':
            word_to_replace = input('Какое слово хотите заменить? ')
            new_word = input('Новое слово? ')
            replace_word(word_to_replace, new_word)
        elif user_input == '3':
            print_text()
        elif user_input == '0':
            print('Выход')
            break

main()