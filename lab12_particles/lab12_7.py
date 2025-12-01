text = [
    'Я лгать не хотел в этом даже себе! Не для того, чтобы матери помочь, я убил — вздор!',
    'Не для того я убил, чтобы, получив средства и власть, сделаться благодетелем человечества.',
    'Вздор! Я просто убил; для себя убил, для себя одного: а там стал ли бы я чьим-нибудь благодетелем или всю жизнь,',
    'как паук, ловил бы всех в паутину и из всех живые соки высасывал, мне, в ту минуту, всё равно должно было быть!..',
    'И не деньги, главное, нужны мне были, Соня, когда я убил; не столько деньги нужны были, как другое…',
    'Мне другое надо было узнать, другое толкало меня под руки: мне надо было узнать тогда, и поскорей узнать, вошь ли я, как все, или человек?',
    'Смогу ли я переступить или не смогу! Осмелюсь ли нагнуться и взять или нет? Тварь ли я дрожащая или право имею…'
]

def process_text(text):
    """
    Находит и удаляет предложение с самым коротким словом из текста.
    
    Args:
        text: список строк, где каждая строка может содержать одно или несколько предложений
    """
    
    sentences = []
    current_sentence = ''
    
    for line in text:
        line = line.strip()
        if not line:
            continue
            
        # Добавляем пробел между строками, если нужно
        if current_sentence and not current_sentence[-1] in (' ', '!', '?', '.', '…', ':'):
            current_sentence += " "
        
        current_sentence += line
        
        # Проверяем, завершено ли предложение
        i = 0
        while i < len(current_sentence):
            char = current_sentence[i]
            
            # Если это конец предложения
            if char in '.!?':
                # Проверяем на многоточие
                if char == '.' and i + 2 < len(current_sentence) and current_sentence[i+1:i+3] == '..':
                    i += 3  # Пропускаем многоточие
                    continue
                
                # Сохраняем предложение
                sentence = current_sentence[:i+1].strip()
                if sentence:
                    sentences.append(sentence)
                
                # Обрезаем текущее предложение
                current_sentence = current_sentence[i+1:].strip()
                i = 0
                continue
            
            # Если это многоточие (символ … или ...)
            elif char == '…' or (char == '.' and i + 1 < len(current_sentence) and current_sentence[i+1] == '.'):
                if char == '.':
                    # Проверяем, действительно ли это многоточие
                    dots_count = 1
                    j = i + 1
                    while j < len(current_sentence) and current_sentence[j] == '.':
                        dots_count += 1
                        j += 1
                    
                    if dots_count >= 3:
                        sentence = current_sentence[:i+dots_count].strip()
                        if sentence:
                            sentences.append(sentence)
                        
                        current_sentence = current_sentence[i+dots_count:].strip()
                        i = 0
                        continue
                else:
                    # Символ многоточия …
                    sentence = current_sentence[:i+1].strip()
                    if sentence:
                        sentences.append(sentence)
                    
                    current_sentence = current_sentence[i+1:].strip()
                    i = 0
                    continue
            
            i += 1
    
    # Добавляем последнее предложение, если оно осталось
    if current_sentence.strip():
        sentences.append(current_sentence.strip())
    
    
    # Находим предложение с самым коротким словом
    shortest_word_len = float('inf')
    shortest_sentence_idx = -1
    shortest_word = ""
    
    for idx, sentence in enumerate(sentences):
        # Разбиваем предложение на слова
        word = ""
        for char in sentence:
            if char.isalpha() or char == '-':
                word += char
            else:
                if word:  # Нашли конец слова
                    word_len = len(word)
                    if word_len < shortest_word_len and word_len > 0:
                        shortest_word_len = word_len
                        shortest_sentence_idx = idx
                        shortest_word = word
                    word = ""
        
        # Проверяем последнее слово в предложении
        if word:
            word_len = len(word)
            if word_len < shortest_word_len and word_len > 0:
                shortest_word_len = word_len
                shortest_sentence_idx = idx
                shortest_word = word
    
    # Выводим результат
    if shortest_sentence_idx != -1:
        print(f"\nНайдено предложение:")
        print(f"Индекс: {shortest_sentence_idx + 1}")
        print(f"Предложение: {sentences[shortest_sentence_idx]}")
        print(f"Самое короткое слово: '{shortest_word}' (длина: {shortest_word_len})")
        print("-" * 80) 
        
    else:
        print("Не удалось найти предложение с короткими словами.")
        

process_text(text)

