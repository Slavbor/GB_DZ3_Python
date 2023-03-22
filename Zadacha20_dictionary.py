word = input("Введите слово: ").upper()
score = 0
diction = {'AEIOULNSTRАВЕИНОРСТ': 1,
           'DGДКЛМПУ': 2,
           'BCMPБГЁЬЯ': 3,
           'FHVWYЙЫ': 4,
           'KЖЗХЦЧ': 5,
           'JXШЭЮ': 8,
           'QZФЩЪ': 10}

for letter in word:
    for keys in diction:
        if letter in keys:
            score += diction[keys]
print(score)
