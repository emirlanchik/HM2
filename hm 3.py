# Покупки на сегодн
today = ['лемон', 'блокнот', 'кола', 'ручка', 'сигареты', 'молоко', 'лампочка']

# Покупки на завтра
tomorrow = ['Всё не съедобное покупки ']

today.pop(4)# Удалить сигареты из списка сегодня

# Добавить все орехи из списка орехов в список сегодня

today.extend(["фисташки", "грецкие орехи"])

# Заменить колу на максым
today[2] = 'максым'

# Вставить миндаль между фисташками и грецкими орехами
today.insert(7, 'миндель')

# Добавить курут в конец списка сегодня
today.append('курут')

# Всё не съедобное переместить в покупки на завтра
tomorrow.append(today.pop(1))
tomorrow.append(today.pop(4))

print(today)# ['блокнот', 'ручка', 'лампочка']
print(tomorrow)# [лемон, максым, молоко, фисташки, миндаль, грецкие орехи, курут]