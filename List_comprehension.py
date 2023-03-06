string = input("Введите текст: ")
text = string.split(' ')
words = [i for i in text if i.isalnum()]
print(' '.join(words))
