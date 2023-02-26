# * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; 
# K – 5 очков; 
# J, X – 8 очков; 
# Q, Z – 10 очков. 
# А русские буквы оцениваются так: 
# А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; 
# Й, Ы – 4 очка; 
# Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков; 
# Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
# *Пример:*
# ноутбук
#     12

score_eng = {1: 'aeioulnstr',\
        2: 'dg', 3: 'bcmp',\
        4: 'fhwvy',\
        5: 'k',\
        8: 'jx',\
        10: 'qz'}

score_rus = {1: 'авеинорст',\
            2: 'дклмпу',\
            3: 'бгёья',\
            4: 'йы',\
            5: 'жзхцч',\
            8: 'шэю',\
            10: 'фщъ'}

w_eng = ['solution', 'qwerty', 'earth']
w_rus = ['привет', 'щавель', 'щебетание']

def eng_count_score(word):
    val = 0
    global score_eng
    for i in range(len(word)):
        for k,v in score_eng.items():
            if word[i] in v:
                val += k
    return val
            
def rus_count_score(word):
    val = 0
    global score_rus
    for i in range(len(word)):
        for k,v in score_rus.items():
            if word[i] in v:
                val += k
    return val

print('РУССКИЕ СЛОВА:')
for i in w_rus:
    print(f'{i} <- ваше слово.\n{rus_count_score(i)} <- стоимость слова.\n')

print('ENGLISH WORDS:')
for i in w_eng:
    print(f'{i} <- ваше слово.\n{eng_count_score(i)} <- стоимость слова.\n')

