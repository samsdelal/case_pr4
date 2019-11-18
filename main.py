from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
syllable = 0
check_cyll = 0
sen = 0
sentence = input('Введите текст: ')
words = len(sentence.split(' '))
alphabet = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
for i in range(len(sentence)):
    sen = sentence.count('.') + sentence.count('?') + sentence.count('!')
print('Предложений:', sen)
print('Слов:', words)



leght = len(sentence)
for i in sentence:
    symb = i.lower()
    if check_cyll <= leght:
        if symb == "a" or symb == "e" or\
            symb == "i" or symb == "o" or\
            symb == "u" or symb == "y" or\
            symb == 'а' or symb == 'у' or\
            symb == 'о' or symb == 'ы' or\
            symb == 'и' or symb == 'э' or\
            symb == 'я' or symb == 'ю' or\
            symb == 'ё' or symb == 'е':
            syllable += 1
            check_cyll += 1
        else:
            check_cyll += 1
    else:
        break

asl = words/sen
asw = syllable/words
fre_ru = 206.835 - (1.3 * asl) - (60.1 * asw)
fre_eng = 206.835 - (1.015 * asl) - (84.6 * asw)

print('Слогов:', syllable)
print('Средняя длина предложения в словах:', asl)
print('Средняя длина слова в слогах:', asw)

if 65 <= ord(sentence[0]) <= 122:
    print('Индекс удобочитаемости Флеша:', fre_eng)
    if 65 < fre_ru <= 100:
        print('Текст очень легко читается (для младших школьников).', )
    elif 30 < fre_ru <= 65:
        print('Текст средней сложности.')
    elif 0 < fre_ru <= 30:
        print('Очень трудно читать.')


elif 1040 <= ord(sentence[0]) <= 1105:
    print('Индекс удобочитаемости Флеша:', fre_ru)
    if 80 < fre_ru <= 100:
        print('Текст очень легко читается (для младших школьников).', )
    elif 50 < fre_ru <= 80:
        print('Текст простой (для школьников)')
    elif 25 < fre_ru <= 50:
        print('Текст, который могут читать выпускники школы.')
    elif 0 <= fre_ru <= 25:
        print('Текст трудно читается (для людей с высшим образованием)')


sentence_b = TextBlob(sentence)
if sentence_b.detect_language() == 'ru':
    sentence_translated = sentence_b.translate(from_lang='ru', to='us')
    sentence_translated = TextBlob(str(sentence_translated))
    if int(sentence_translated.polarity) < 0:
        print('Тональность текста: ', 'Не нейтральный')
    else:
              print('Тональность текста: ', 'Нейтральный')
    print('Объективность: ', 100 - sentence_translated.subjectivity * 100, '%')
else :
    if int(sentence_b.polarity) < 0:
        print('Тональность текста: ', 'Не нейтральный')
    else:
        print('Тональность текста: ', 'Нейтральный')
    print('Объективность: ', 100 - sentence_b.subjectivity * 100, '%')




