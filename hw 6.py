''' Пользователь загадывает число до 100, а программа должна угадать это число за
минимальное количество попыток. Программа дложна выдавать числа, а пользователь отвечать
больше, меньше или да
'''
from random import randint
low = 1
high = 100
guess = randint(low, high)
print(guess)
my_answer = ''
while my_answer != 'da':
    my_answer = input()
    if my_answer == "bolshe":
        low = guess
        guess = randint(guess, high)
        print(guess)

    elif my_answer == 'menshe':
        high = guess
        guess = randint(low, guess)
        print(guess)
    else:
        print('sdelano')