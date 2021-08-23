''' Пользователь загадывает число до 100, а программа должна угадать это число за
минимальное количество попыток. Программа дложна выдавать числа, а пользователь отвечать
больше, меньше или да
'''
low = 1
high = 100
guess = (low + high)//2
print(guess)
my_answer = ''
while my_answer != 'da':
    my_answer = input()
    if my_answer == "bolshe":
        low = guess
        guess = (low + high)//2
        print(guess)

    elif my_answer == 'menshe':
        high = guess
        guess = (low + high)//2
        print(guess)
    else:
        print('sdelano')
