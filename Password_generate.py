import random


symbols = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

password_len = input('Введите длину пароля: ')
while not password_len.isdigit():
    print("Вы ввели не число!")
    password_len = input('Введите длину пароля: ')

done = ''
for i in range(int(password_len)):
    done += random.choice(symbols)
print(done)