''' Пользователь загадывает число до 100, а программа должна угадать это число за
минимальное количество попыток. Программа дложна выдавать числа, а пользователь отвечать
больше, меньше или да
'''
start = 0
end = 100
count = 0

while True:
    center = (start + end) // 2
    count += 1
    answer = input(f'твой номер: {center}? | greater/less/yes ')
    if answer == 'yes':
        print(f'Guessed in {count} attempts!')
        break
    elif answer == 'g':
        start = center + 1
    elif answer == 'l':
        end = center - 1
