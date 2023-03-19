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
print('info:Решение через строки')
print()
word = input("Введите слово: ")
word_capital = word.upper()
count = 0
point_1 = 'AEIOULNSTRАВЕИНОРСТ'
point_2 = 'DGДКЛМПУ'
point_3 = 'BCMPБГЁЬЯ'
point_4 = 'FHVWYЙЫ'
point_5 = 'KЖЗХЦЧ'
point_8 = 'JXШЭЮ'
point_10 = 'QZФЩЪ'

for elem in word_capital:
    if elem in point_1:
        count += 1
        word_capital = word_capital.replace(elem, '', 1)
for elem in word_capital:
    if elem in point_2:
        count += 2
        word_capital = word_capital.replace(elem, '', 1)
for elem in word_capital:
    if elem in point_3:
        count += 3
        word_capital = word_capital.replace(elem, '', 1)
for elem in word_capital:
    if elem in point_4:
            count += 4
            word_capital = word_capital.replace(elem, '', 1)
for elem in word_capital:
    if elem in point_5:
            count += 5
            word_capital = word_capital.replace(elem, '', 1)
for elem in word_capital:
    if elem in point_8:
            count += 8
            word_capital = word_capital.replace(elem, '', 1)
            break
for elem in word_capital:
    if elem in point_10:
            count += 10
            word_capital = word_capital.replace(elem, '', 1)
print(f"Количество очков за слово: {count}")