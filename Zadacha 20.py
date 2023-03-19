# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит
# либо только английские, либо только русские буквы.
#
# *Пример:*
#
# ноутбук
#     12
print('info: Программа преобразует все буквы слова в заглавные, при нахождении буквы в списке соответствующему очку,')
print("считает количество очков, и для ускорения выполнения удаляет эту букву из слова и переходит на следующую букву.")
print()
word = input("Введите слово: ")
word_capital = word.upper()
count = 0
point_1_list = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
point_2_list = ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У']
point_3_list = ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я']
point_4_list = ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы']
point_5_list = ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч']
point_8_list = ['J', 'X', 'Ш', 'Э', 'Ю']
point_10_list = ['Q', 'Z', 'Ф', 'Щ', 'Ъ']

for elem in word_capital:
    for element in point_1_list:
        if elem == element:
            count += 1
            word_capital = word_capital.replace(elem, '', 1)
            break
for elem in word_capital:
    for element in point_2_list:
        if elem == element:
            count += 2
            word_capital = word_capital.replace(elem, '', 1)
            break
for elem in word_capital:
    for element in point_3_list:
        if elem == element:
            count += 3
            word_capital = word_capital.replace(elem, '', 1)
            break
for elem in word_capital:
    for element in point_4_list:
        if elem == element:
            count += 4
            word_capital = word_capital.replace(elem, '', 1)
            break
for elem in word_capital:
    for element in point_5_list:
        if elem == element:
            count += 5
            word_capital = word_capital.replace(elem, '', 1)
            break
for elem in word_capital:
    for element in point_8_list:
        if elem == element:
            count += 8
            word_capital = word_capital.replace(elem, '', 1)
            break
for elem in word_capital:
    for element in point_10_list:
        if elem == element:
            count += 10
            word_capital = word_capital.replace(elem, '', 1)
            break
print(f"Количество очков за слово: {count}")