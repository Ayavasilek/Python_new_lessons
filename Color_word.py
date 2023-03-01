from colorama import Fore
string = input('Введите текст: ')
text = string.split()
result = ''
for color_word in text:
    if color_word.istitle():
        result += Fore.GREEN
    else:
        result += Fore.RESET
    result += color_word + ''
print(result)