#Задача 16
count = 0
some_list = [int(input('Введите элемент списка: ')) for _ in range(int(input('Введите количество элементов в списке: ')))]
x = int(input('Введите значение элемента для поиска: '))
for i in range(0, len(some_list) - 1):
    if some_list[i] == x:
        count += 1
print(count)