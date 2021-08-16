# Создайте массив состоящий из словарей с данными классов/аудиторий Гиктека
home = [
    {
       'name' : 'Empo',
        'room' : 1,
        'sit' : False
    },
    {
        'name' : 'lala',
        'room' : 2,
        'sit' : False
    },
    {
        'name' : 'Nana',
        'room' : 3,
        'sit' : False
    },
]

free_rooms = []

# Напишите функцию которая принимает ранее созданный массив, фильтрирует
# полученный массив и возвращающает не менне двух элементов из массива
def check_sit(home):
    for free_room in home:
        if free_room['sit'] == False:
            print('комната #', free_room['name'], 'нету')
            free_rooms.append(free_room)
check_sit(home)
# Напишите функцию которая принимает отфильтрованные данные, добавляет
# новое значение каждому из элементов отфильтрованных данных и возвращает
# измененные данные с добавленными значениями
def reserve_third_home(home):
    for home in home:
        if home['room'] == 3:
            home['sit'] = True
            print("она дома сидит и чилит", home)
reserve_third_home(free_rooms)
# Напишите функцию которая принимает массив ранее измененых данных,
# меняет значение в каждом из элементов и возращает измененные данные


# Напишите функцию которая принимает массив ранее измененых данных,
# и поочередно выводит их в консоль
def show_in_console(room):
    for home in room:
        print(home)
show_in_console(free_rooms)