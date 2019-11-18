from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

sentence = input('Введите текст: ')
sen = len(sentence.split('.')) - 1
words = len(sentence.split(' '))
alphabet = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
print('Предложений  - ', sen)
print('Слов - ', words)
analise = TextBlob(sentence)
print(analise.sentiment)

