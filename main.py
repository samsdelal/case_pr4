from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
syllable = 0
check_cyll = 0

sentence = input('Введите текст: ')
sen = len(sentence.split('.')) - 1
words = len(sentence.split(' '))
alphabet = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
print('Предложений:', sen)
print('Слов:', words)
#analise = TextBlob(sentence)
#print(analise.sentiment) #Артем не знает что это

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

print('Слогов:', syllable)
print('Средняя длина предложения в словах:', words/sen)
print('Средняя длина слова в слогах:', syllable/words)
print('Индекс удобочитаемости Флеша:', )
print('Текст очень легко читается (для младших школьников).', )
print('Тональность текста:', )

