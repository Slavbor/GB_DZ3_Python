# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине
# элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5
import random
print("Программа ищет ближайшее число, и еще одно, если есть такое же равноудаленное, но в противоположную строну.")
print("(Пример: ищем 5, а в списке есть 3 и 7)")
number = int(input("Введите размер списка: "))
print
list = [random.randint(0, 20) for _ in range(number)]
print(list)
num_find_x = int(input("Введите число для поиска ближайших чисел из списка: "))
unique_list = []
unique_list2 = []
for elem in list:
    if elem not in unique_list and elem != num_find_x:
        unique_list.append(elem)
nearst = unique_list[0]
nearst2 = unique_list[0]

for i in range(len(unique_list)):
    if abs(num_find_x - unique_list[i]) < abs(num_find_x - nearst):
        nearst = unique_list[i]
for elem in unique_list:
    if elem not in unique_list2 and elem != nearst:
        unique_list2.append(elem)
for elem in unique_list2:
    if abs(elem - num_find_x) == abs(num_find_x - nearst):
        nearst2 = elem

if abs(num_find_x - nearst) == abs(num_find_x - nearst2) and nearst != nearst2:
    print()
    print(f"Ближайшие числа к {num_find_x} из списка: {nearst} и {nearst2} ")
else:
    print()
    print(f"Ближайшее число к {num_find_x} из списка: {nearst}")
