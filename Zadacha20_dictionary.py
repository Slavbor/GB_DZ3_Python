word = input("Введите слово: ").upper()
score = 0
diction = {('А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т', 'A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'): 1,
       ('Д', 'К', 'Л', 'М', 'П', 'У', 'D', 'G'): 2,
       ('Б', 'Г', 'Ё', 'Ь', 'Я', 'B', 'C', 'M', 'P'): 3,
       ('Й', 'Ы', 'F', 'H', 'V', 'W', 'Y'): 4,
       ('Ж', 'З', 'Х', 'Ц', 'Ч', 'K'): 5,
       ('Ш', 'Э', 'Ю', 'J', 'X'): 8,
       ('Ф', 'Щ', 'Ъ', 'Q', 'Z'): 10}

for keys, value in diction.items():
    for letter in word:
        if letter in keys:
            score += value
print(score)
